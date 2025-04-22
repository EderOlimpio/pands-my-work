
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

---

## References

- Bishop, M. (2003). Computer security: Art and science. Addison-Wesley.

- Downey, A. (2015). Think Python: How to Think Like a Computer Scientist (2nd ed.). O’Reilly Media.

- GitHub. (n.d.). Creating a new repository. GitHub Docs. Retrieved from https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository

- Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... & Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585(7825), 357–362. https://doi.org/10.1038/s41586-020-2649-2

- Hildebrand, F. B. (1987). Introduction to Numerical Analysis. Dover Publications.

- Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55

- Lagarias, J. C. (2006). The 3x+1 Problem: An Annotated Bibliography (1963–1999). arXiv preprint arXiv:math/0309224. https://arxiv.org/abs/math/0309224

- Newton's method. (n.d.). In Wikipedia. Retrieved from https://en.wikipedia.org/wiki/Newton%27s_method

- OWASP Foundation. (n.d.). OWASP Top Ten. Retrieved from https://owasp.org/www-project-top-ten/

- Python Software Foundation. (2023). Python Language Reference, version 3.11. Retrieved from https://docs.python.org/3/reference/

- Python Software Foundation. (n.d.). datetime — Basic date and time types. Python 3.12 Documentation. Retrieved from https://docs.python.org/3/library/datetime.html

- Python Software Foundation. (n.d.). datetime.date.weekday() method. Python 3.12 Documentation. Retrieved from https://docs.python.org/3/library/datetime.html#datetime.date.weekday

- Python Software Foundation. (n.d.). Errors and exceptions. Python 3 documentation. Retrieved from https://docs.python.org/3/tutorial/errors.html

- Python Software Foundation. (n.d.). Formatted string literals (f-strings). Retrieved from https://docs.python.org/3/reference/lexical_analysis.html#f-strings

- Python Software Foundation. (n.d.). open() — Built-in function. Python 3 documentation. Retrieved from https://docs.python.org/3/library/functions.html#open

- Python Software Foundation. (n.d.). str.count() — String method. Python 3 documentation. Retrieved from https://docs.python.org/3/library/stdtypes.html#str.count

- Python Software Foundation. (n.d.). sys — System-specific parameters and functions. Python 3 documentation. Retrieved from https://docs.python.org/3/library/sys.html

- Python Software Foundation. (n.d.). What does if name == 'main' do?. Python FAQ. Retrieved from https://docs.python.org/3/library/main.html

- Sastry, S. S. (2003). Numerical Methods: A Practical Approach. Prentice Hall.

- Sedgewick, R., & Wayne, K. (2016). Introduction to Programming in Python: An Interdisciplinary Approach. Addison-Wesley.

- Stallings, W. (2018). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson.

- van Rossum, G., Warsaw, B., & Coghlan, N. (2001). PEP 8 – Style guide for Python code. Python Enhancement Proposals. Retrieved from https://peps.python.org/pep-0008/

- Zelle, J. (2016). Python Programming: An Introduction to Computer Science (3rd ed.). Franklin, Beedle & Associates Inc.


 

