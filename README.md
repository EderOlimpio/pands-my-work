
# pands-my-work

A collection of beginner-friendly Python scripts that demonstrate core programming concepts such as control flow, file handling, user input, error handling, and data visualization.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Script Descriptions](#script-descriptions)
  - [accounts.py](#accountspy)
  - [bank.py](#bankpy)
  - [collatz.py](#collatzpy)
  - [es.py](#espy)
  - [first_program.py](#first_programpy)
  - [plottask.py](#plottaskpy)
  - [squareroot.py](#squarerootpy)
  - [weekday.py](#weekdaypy)
- [License](#license)

---

## Project Structure

This repository includes the following Python files:

- `accounts.py`: Mask sensitive digits in account numbers.
- `bank.py`: Add two amounts (in cents) and format output in euros and cents.
- `collatz.py`: Compute the Collatz sequence for a given integer.
- `es.py`: Count occurrences of the letter "e" in a text file.
- `first_program.py`: Print "Hello, world!" to the console.
- `plottask.py`: Plot a histogram and a cubic function using matplotlib.
- `squareroot.py`: Approximate square roots using Newton's method.
- `weekday.py`: Determine if today is a weekday or weekend.

---

## Getting Started

1. **Clone or download this repository** to your local machine.
2. **Ensure Python 3 is installed** on your system.
3. **Install dependencies** for scripts that require external libraries:
   ```bash
   pip install numpy matplotlib

---

## Script Descriptions

### `accounts.py`

Masks digits in account numbers using two methods:
- For 10-digit account numbers, masks all digits except the last 4.
- For account numbers of any length, masks all digits except the last one.

**Usage:**
```bash
python accounts.py
```
You will be prompted to enter an account number. The masked version will be printed.

### `bank.py`

Adds two amounts (in cents), then outputs the result in euros and cents.

**Usage:**
```bash
python bank.py
```

Enter two amounts in cents when prompted.

### `collatz.py`

Implements the Collatz sequence for a given positive integer.

**Usage:**
```bash
python collatz.py
```

Enter a positive integer when prompted. The script will print the sequence.

### `es.py`

Counts the number of lowercase ```'e'``` characters in a text file provided as a command-line argument.

**Usage:**
```bash
python es.py <filename>
```

Handles missing files and decoding errors gracefully.

### `first_program.py`

A simple "Hello, world!" script.

**Usage:**
```bash
python first_program.py
```

### `plottask.py`

Generates and displays a plot with:

- A histogram of 1000 normally distributed values (mean=5, std=2)

- The function h(x)=x3
 

**Requirements:**
- ```numpy```
- ```matplotlib```

**Usage:**
```bash
pip install numpy matplotlib
python plottask.py
```

The plot is saved as ```plot_output.png``` and also displayed.

### `squareroot.py`

Approximates the square root of a positive number using Newton's method.

***Usage:***
```bash
python squareroot.py
```

Enter a positive number when prompted. The result is shown to six decimal places.

### `weekday.py`
Checks the current day and prints whether it's a weekday or weekend.

***Usage:***
```bash
python weekday.py
```




 

