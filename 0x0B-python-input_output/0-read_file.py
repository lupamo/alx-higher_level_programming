#!/usr/bin/python3
"""
a function that reads a file
Returns, printed file
"""


def read_file(filename=""):
    """Reads a file"""

    try:
        with open(f'{filename}', 'r', encoding="utf-8") as f:
            file_read = f.read()
            print(file_read)
    except FileNotFoundError:
        print(f"{filename} doesn't exist")