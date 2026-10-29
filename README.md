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
1. Open the `Task1_Hangman` folder in the terminal.
2. Run:

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

**Note:** The current stock prices are sample values, not live market prices.

**How to Run**
1. Open the `Task2_StockPortfolio` folder in the terminal.
2. Run:

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

3. Enter the path of the folder you want to organize.

**Reference:** [Official Python shutil Documentation](https://docs.python.org/3/library/shutil.html)

**Note:** Choose your target folder carefully because the program moves files into category folders.



### Task 5: Enterprise Smart Inventory & Asset System

An object-oriented Python application for managing books, magazines, and digital media. It demonstrates core OOP concepts through an inventory management system.

**Features**
- Uses an abstract base class named `LibraryItem`.
- Implements `Book`, `Magazine`, and `DigitalMedia` subclasses.
- Demonstrates inheritance, abstraction, encapsulation, and polymorphism.
- Uses private attributes and property-based price validation.
- Implements `__str__`, `__repr__`, `__eq__`, and `__len__` magic methods.
- Supports adding items and checking out and returning inventory items.
- Calculates late fees according to item type.
- Generates a tabular inventory display and an audit report.
- Handles duplicate item IDs, invalid item IDs, and invalid late-day inputs.

**Technologies Used**
- Python 3
- `abc` module
- `datetime` module
- Object-oriented programming
- Properties and validation
- Magic methods
- Exception handling

**How to Run**
1. Open the `Task5_SmartInventory` folder in the terminal.
2. Run:

   `python inventory.py`

3. Use the menu to display inventory, check out items, return items, or generate an audit report.

**Reference:** [Official Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)

**Note:** The late-fee amounts are example rules used for this project.

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
├── Task3_FileOrganizer/
│   └── organizer.py
└── Task5_SmartInventory/
    ├── models.py
    └── inventory.py
```

## Internship Goal

To improve Python programming skills by building practical projects, applying programming concepts, solving problems, and documenting the work completed during the internship.
