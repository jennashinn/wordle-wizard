def filter_wordle_words(words, guesses):
    """
    Filters the word list based on Wordle guesses.

    :param words: List of possible words.
    :param guesses: List of guesses, where each guess is a dictionary:
        {'letters': ['s', 'o', 'a', 'r', 'e'], 'status': ['Green', 'Gray', 'Yellow', 'Gray', 'Gray']}
    :return: List of filtered words.
    """
    green_positions = [""] * 5  # Track Green letters by position
    yellow_positions = [set() for _ in range(5)]  # Track Yellow letters by position
    gray_positions = [set() for _ in range(5)]  # Track Gray letters by position
    global_green_yellow = set()  # Globally allowed letters (Green or Yellow)
    global_gray = set()  # Globally disallowed letters (Gray)

    # Process each guess
    for guess in guesses:
        letters = guess["letters"]
        status = guess["status"]

        for i, (letter, state) in enumerate(zip(letters, status)):
            if state == "Green":
                # Track Green letters for the exact position
                green_positions[i] = letter
                global_green_yellow.add(letter)
            elif state == "Yellow":
                # Track Yellow letters and ensure they do not appear in the current position
                yellow_positions[i].add(letter)
                global_green_yellow.add(letter)
            elif state == "Gray":
                # Only add to Gray if not already in Green or Yellow
                if letter not in global_green_yellow:
                    global_gray.add(letter)
                    gray_positions[i].add(letter)

    # Apply Green constraints
    for i, letter in enumerate(green_positions):
        if letter:
            words = [word for word in words if word[i] == letter]

    # Apply Yellow constraints
    for i, yellow_set in enumerate(yellow_positions):
        for letter in yellow_set:
            # Letter must appear in the word but not in this position
            words = [word for word in words if letter in word and word[i] != letter]

    # Apply Gray constraints by position
    for i, gray_set in enumerate(gray_positions):
        for letter in gray_set:
            # Exclude this Gray letter only from this position
            words = [word for word in words if word[i] != letter]

    # Apply Global Gray Exclusion
    # Remove any word containing a globally `Gray` letter unless that letter is required (Green/Yellow)
    for letter in global_gray:
        if letter not in global_green_yellow:
            words = [word for word in words if letter not in word]

    return words


from collections import Counter
def suggest_best_words(filtered_words, num_suggestions=5):
    """
    Suggests the most likely words based on letter frequency.

    :param filtered_words: List of possible words after filtering.
    :param num_suggestions: Number of words to suggest (default: 5).
    :return: List of the top suggested words.
    """
    if not filtered_words:
        return []

    # Count letter frequencies across all possible words
    letter_counts = Counter(letter for word in filtered_words for letter in word)

    # Rank words based on sum of letter frequencies (prioritizing unique letters)
    def word_score(word):
        return sum(letter_counts[letter] for letter in set(word))  # Unique letters only

    # Sort words by score in descending order
    ranked_words = sorted(filtered_words, key=word_score, reverse=True)

    # Return the top `num_suggestions` words
    return ranked_words[:num_suggestions]
