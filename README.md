Datheon Python Internship

Python programming internship projects completed as part of the Datheon Python Programming Internship.

Tasks

Task 1: Hangman Word Guessing Game

A beginner-friendly, console-based word guessing game developed using Python.

Features

- Random word selection from a word list.
- Displays hidden letters using underscores.
- Accepts one letter at a time.
- Allows up to 6 incorrect guesses.
- Prevents duplicate guesses from counting as mistakes.
- Displays hangman stages as incorrect guesses increase.
- Shows a win or loss message at the end.

Technologies Used

- Python 3
- "random" module
- File handling
- Sets and loops

How to Run

1. Open the "Task1_Hangman" folder in the terminal.

2. Run:
   
   "python hangman.py"

Keep "words.txt" in the same folder as "hangman.py".

Task 2: Stock Portfolio Performance Tracker

A Python program that calculates stock investment values, profit or loss, and percentage changes, then saves the results to a CSV report.

Features

- Loads S&P 500 company tickers from a CSV dataset.
- Checks whether portfolio tickers exist in the dataset.
- Calculates total investment and current portfolio value.
- Calculates profit or loss and percentage change for each stock.
- Generates a "portfolio_summary.csv" report.
- Displays the overall portfolio summary in the terminal.

Technologies Used

- Python 3
- "csv" module
- Dictionaries and loops
- File handling

Note: The current stock prices are sample values, not live market prices.

How to Run

1. Open the "Task2_StockPortfolio" folder in the terminal.

2. Run:
   
   "python portfolio.py"

Keep "constituents.csv" in the same folder as "portfolio.py". The program generates "portfolio_summary.csv" when it runs.

Task 4: Rule-Based Interactive Terminal Assistant / Chatbot

A rule-based conversational chatbot developed using Python. It recognizes user intents through keywords and regular expressions and provides relevant responses to common questions.

Features

- Recognizes multiple user intents.
- Handles questions about business hours and product FAQs.
- Uses keywords and regular expressions to understand user input.
- Provides contextual responses to user queries.
- Uses a JSON file to store sample FAQ data.
- Includes fallback responses for unrecognized questions.
- Supports exit commands such as "bye", "exit", and "quit".
- Runs interactively in the terminal.

Technologies Used

- Python 3
- "re" module for regular expressions
- "json" module for FAQ data
- Dictionaries and conditional statements
- Functions and loops
- String processing

How to Run

1. Open the "Task4_Chatbot" folder in the terminal.

2. Run:
   
   "python chatbot.py"

Keep "sample_faq.json" in the same folder as "chatbot.py".

Example Interaction

Chatbot: Hello! Welcome to our customer support assistant.
You: What are your business hours?
Chatbot: Our business hours are 9 AM to 6 PM.
You: Tell me about your products.
Chatbot: Please check our product FAQs for more information.
You: bye
Chatbot: Goodbye! Have a nice day.

Note: The example responses above are illustrative. Actual responses depend on the rules and FAQ data implemented in the chatbot.

Project Structure

Datheon_Python_Internship/
├── README.md
├── Task1_Hangman/
│   ├── hangman.py
│   └── words.txt
├── Task2_StockPortfolio/
│   ├── portfolio.py
│   ├── constituents.csv
│   └── portfolio_summary.csv
└── Task4_Chatbot/
    ├── chatbot.py
    └── sample_faq.json

Internship Goal

To improve Python programming skills by building practical projects, applying programming concepts, solving problems, and documenting the work completed during the internship.
