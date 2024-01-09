#!/usr/bin/python3
"""
a function that reads a file
Returns, printed file
"""


def read_file(filename=""):
    """Reads a file"""

    with open(f'{filename}', 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="\n")
