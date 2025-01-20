# Wordle Solver

## Overview
This **Wordle Solver** is a Flask-based web application that helps users strategically solve the popular word game *Wordle*. The app allows users to input their guesses, select letter statuses (green, yellow, or gray), and filter the list of possible words dynamically. Additionally, the solver provides the **best word suggestions** based on common letter usage to maximize guessing efficiency.

## Features
✅ **Dynamic Word Filtering** – Narrows down possible words based on user input.  
✅ **Best Word Suggestions** – Recommends the top 5 words based on letter frequency.  
✅ **Automatic Letter Coloring** – Background changes dynamically based on selection.  
✅ **Reset Button** – Quickly restart and enter a new Wordle game.  
✅ **Scrollable Word List** – Keeps UI clean while displaying all possible words.  
✅ **Responsive UI** – Optimized layout for easy use.  

## Deployment
This app is deployed on [Render/Railway/Fly.io] (**Update with actual link**) so users can access it online without running it locally.

## Installation & Setup
If you want to run the solver locally, follow these steps:

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate    # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**
```sh
python app.py
```
The app will run on `http://127.0.0.1:5000/` by default.

## Usage
1. **Enter your Wordle guesses in the grid**.
2. **Select letter statuses** using the color-coded buttons.
3. **Click "Find Words"** to filter possibilities.
4. **Use "Best Suggestions"** to make the next optimal guess.
5. **Click "Reset"** to start a new game.

## Technologies Used
- **Python** (Flask)
- **HTML, CSS** (for UI)
- **JavaScript** (for interactivity)

## Contributing
Feel free to submit pull requests or open issues for suggestions and improvements.

## License
This project is licensed under the MIT License.


