#!/usr/bin/python3
"""
a function that reads a file
Returns, printed file
"""


def read_file(filename=""):
    """Reads a file
    Args:
    filename: the name of file to be read
    """

    with open(f'{filename}', 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
