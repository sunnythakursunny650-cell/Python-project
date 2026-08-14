🎮 Rock Paper Scissors Game

A professional and interactive Rock Paper Scissors Game built with Python and Streamlit.

This project includes both a console-based Python version and a professional Streamlit web application with live scores, round history, match results, and CSV report download.

🚀 Live Demo

🔗 Streamlit Live App: Coming Soon(https://python-project-e9app8raqvnz9zbq28yubvw.streamlit.app)
✨ Features

- 🎮 Interactive Rock Paper Scissors gameplay
- 👤 Player name input
- 🎯 Best of 3 or Best of 5 rounds
- 🪨 Rock
- 📄 Paper
- ✂️ Scissors
- 🤖 Random computer moves
- 🏆 Automatic winner detection
- 📊 Live scoreboard
- 🤝 Tie tracking
- 📜 Round-by-round history
- 📥 Download match report as CSV
- 🔄 New Game option
- 🎉 Match winner celebration
- ⚠️ Input validation
- 💻 Console version
- 🌐 Streamlit web application
- 📱 Clean and responsive interface

🛠️ Technologies Used

- Python 3
- Streamlit
- Pandas
- Random Module

📂 Project Structure

Rock-Paper-Scissors/
│
├── simple_game.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

🎮 Game Rules

The game follows the classic Rock Paper Scissors rules:

- 🪨 Rock beats Scissors
- 📄 Paper beats Rock
- ✂️ Scissors beats Paper
- 🤝 Same choices result in a Tie

🏆 Scoring System

Each round gives one point to the winner.

At the end of the selected rounds:

- 🥇 Higher score → Match Winner
- 🤝 Equal scores → Match Draw

💻 Console Version

The original Python console version is available in:

simple_game.py

Run the console version:

python simple_game.py

🌐 Streamlit Web Application

The professional web version is available in:

app.py

Run the application locally:

streamlit run app.py

📊 Match History

After every round, the application records:

- Round number
- Player choice
- Computer choice
- Round result

The complete match history can be viewed inside the application.

📥 Download Match Report

After playing the match, users can download the complete round history as a CSV file.

Example report:

Round,Your Choice,Computer Choice,Result
1,Rock,Scissors,Player
2,Paper,Paper,Tie
3,Scissors,Rock,Computer

🚀 Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Open the project folder:

cd Rock-Paper-Scissors

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

🎯 Project Objective

The main objective of this project is to demonstrate practical Python programming and Streamlit development through an interactive game application.

Concepts Demonstrated

- Python functions
- Conditional statements
- Loops
- Randomization
- Input validation
- Score management
- Session state
- Data handling
- CSV generation
- Streamlit UI development

🔮 Future Enhancements

- 🏅 Player leaderboard
- 💾 Persistent match history
- 📈 Advanced statistics
- 👥 Two-player mode
- 🎨 Custom themes
- 🔊 Sound effects
- 🏆 Tournament mode

👨‍💻 Author

Sunny Thakur

Python Developer | Aspiring Data Scientist | Machine Learning Enthusiast

---

⭐ If you find this project useful, consider giving the repository a star!

Thank you for visiting this project! 🎮
