# Python Expense Tracker 💰🐍

A simple command-line expense tracker built with Python. It allows users to add expenses, view their expenses, calculate total spending, and exit the program.

## Features

* ➕ Add expenses
* 🏷️ Assign expenses to categories
* 👀 View recorded expenses
* 🧮 Calculate total spending
* 🔄 Add multiple expenses
* 🚪 Exit the program
* ⚠️ Handles invalid menu choices

## How It Works

The program uses a Python dictionary to store each expense:

```python
expenses[category] = amount
```

The total spending is calculated using:

```python
sum(expenses.values())
```

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the program:

```bash
python expense_tracker.py
```

5. Choose an option from the menu.

## Example

```text
===== EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. Show total
4. Exit

Choose an option: 1

Enter category: Food
Enter amount: 12.50

Expense added!

Choose an option: 1

Enter category: Transport
Enter amount: 5.00

Expense added!

Choose an option: 3

Total spent: 17.5
```

## Technologies Used

* Python
* Dictionaries
* `while` loops
* `if/elif/else` statements
* User input
* `sum()` function

## What I Learned

This project helped me practice:

* Working with dictionaries
* Storing key-value pairs
* Using loops to create a menu system
* Using conditional statements
* Calculating totals from dictionary values
* Building an interactive command-line application
