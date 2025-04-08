"""
es.py - Count the number of lowercase 'e' characters in a text file.

Usage:
    python es.py <filename>

Handles:
    - Missing argument
    - File not found
    - File not readable (not text)
"""

import sys

def main():
    # Check if filename argument was provided
    if len(sys.argv) < 2:
        print("Error: No filename provided.")
        print("Usage: python es.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            e_count = contents.count('e')
            print(e_count)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: File '{filename}' is not a valid text file (could not decode).")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()


# References:

# Python Software Foundation. (n.d.). sys — System-specific parameters and functions. Python 3 documentation. https://docs.python.org/3/library/sys.html
# Python Software Foundation. (n.d.). open() — Built-in function. Python 3 documentation. https://docs.python.org/3/library/functions.html#open
# Python Software Foundation. (n.d.). str.count() — String method. Python 3 documentation. https://docs.python.org/3/library/stdtypes.html#str.count
# Python Software Foundation. (n.d.). Errors and exceptions. Python 3 documentation. https://docs.python.org/3/tutorial/errors.html
# GitHub. (n.d.). Creating a new repository. GitHub Docs. https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
# van Rossum, G., Warsaw, B., & Coghlan, N. (2001). PEP 8 – Style guide for Python code. Python Enhancement Proposals. https://peps.python.org/pep-0008/

