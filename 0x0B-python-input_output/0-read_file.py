#!/usr/bin/python3
"""
a function that reads a file
Returns, printed file
"""


def read_file(filename=""):
    """Reads a file"""

    with open(f'{filename}', 'r', encoding="UTF8") as f:
        print(f.read())
