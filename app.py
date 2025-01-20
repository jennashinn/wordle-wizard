from flask import Flask, render_template, request, jsonify
from wordle_solver import filter_wordle_words, suggest_best_words  # Import the function

app = Flask(__name__)

# Load the word list once at startup
with open("word_list.txt") as f:
    word_list = [line.strip() for line in f if len(line.strip()) == 5]

@app.route("/")
def index():
    # Compute the best 5 starting words based on frequency
    best_starting_words = suggest_best_words(word_list, num_suggestions=5)
    return render_template("index.html", best_starting_words=best_starting_words)


@app.route("/filter_words", methods=["POST"])
def filter_words():
    data = request.json
    guesses = data.get("guesses", [])

    # Apply the filtering function
    filtered_words = filter_wordle_words(word_list, guesses)

    # Sort the filtered words alphabetically
    filtered_words = sorted(filtered_words)

    # Get the top 5 best word suggestions
    suggested_words = suggest_best_words(filtered_words, num_suggestions=5)

    return jsonify({"filtered_words": filtered_words, "suggested_words": suggested_words})

if __name__ == "__main__":
    app.run(debug=True)
