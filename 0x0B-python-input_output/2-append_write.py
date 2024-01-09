#!/usr/bin/python3
"""
A function that appends strings
to a text file
"""


def append_write(filename="", text=""):
    """appending a text on file"""

    with open(f'f{filename}', 'a', encoding="UTF8") as f:
        return f.write(text)
