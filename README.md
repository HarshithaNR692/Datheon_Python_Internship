# Datheon Python Internship

Python programming internship projects completed as part of the Datheon Python Programming Internship.

## Tasks

### Task 1: Hangman Word Guessing Game

A beginner-friendly, console-based word guessing game developed using Python.

**Features**
- Random word selection from a word list.
- Displays hidden letters using underscores.
- Accepts one letter at a time.
- Allows up to 6 incorrect guesses.
- Prevents duplicate guesses from counting as mistakes.
- Displays hangman stages as incorrect guesses increase.
- Shows a win or loss message at the end.

**Technologies Used**
- Python 3
- `random` module
- File handling
- Sets and loops

**How to Run**
1. Make sure Python 3 is installed.
2. Open the `Task1_Hangman` folder in the terminal.
3. Run:

   `python hangman.py`

Keep `words.txt` in the same folder as `hangman.py`.

### Task 2: Stock Portfolio Performance Tracker

A Python program that calculates stock investment values, profit or loss, and percentage changes, then saves the results to a CSV report.

**Features**
- Loads S&P 500 company tickers from a CSV dataset.
- Checks whether portfolio tickers exist in the dataset.
- Calculates total investment and current portfolio value.
- Calculates profit or loss and percentage change for each stock.
- Generates a `portfolio_summary.csv` report.
- Displays the overall portfolio summary in the terminal.

**Technologies Used**
- Python 3
- `csv` module
- Dictionaries and loops
- File handling

**Note:** The current stock prices used in this project are sample values, not live market prices.

**How to Run**
1. Make sure Python 3 is installed.
2. Open the `Task2_StockPortfolio` folder in the terminal.
3. Run:

   `python portfolio.py`

Keep `constituents.csv` in the same folder as `portfolio.py`. The program generates `portfolio_summary.csv` when it runs.

### Task 3: Automated File Organizer & Cleanup Utility

A Python utility that organizes files into separate folders based on their file extensions.

**Features**
- Organizes files into Documents, Images, Videos, Archives, and Code folders.
- Scans the selected folder for files.
- Creates category folders automatically.
- Moves supported files using `shutil.move()`.
- Avoids overwriting files when duplicate filenames exist.
- Handles permission and file operation errors.
- Displays a summary of moved, skipped, and failed files.

**Technologies Used**
- Python 3
- `os` module
- `shutil` module
- `pathlib` module
- Exception handling

**How to Run**
1. Open the `Task3_FileOrganizer` folder in the terminal.
2. Run:

   `python organizer.py`

3. Enter the path of the folder you want to organize when prompted.

**Reference:** [Official Python shutil Documentation](https://docs.python.org/3/library/shutil.html)

**Note:** Choose your target folder carefully because the program moves files into category folders.

## Project Structure

```text
Datheon_Python_Internship/
├── README.md
├── Task1_Hangman/
│   ├── hangman.py
│   └── words.txt
├── Task2_StockPortfolio/
│   ├── portfolio.py
│   ├── constituents.csv
│   └── portfolio_summary.csv
└── Task3_FileOrganizer/
    └── organizer.py
```

## Internship Goal

To improve Python programming skills by building practical beginner-level projects and documenting the work completed during the internship.