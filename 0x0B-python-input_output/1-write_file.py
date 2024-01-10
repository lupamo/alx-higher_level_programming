#!/usr/bin/python3
"""
A function that writes on an object file
"""


def write_file(filename="", text=""):
    """Writing on a file
    Args:
    filename: file to write to
    text: what to write on file
    """

    with open(f'{filename}', 'w', encoding="UTF8") as f:
        return f.write(text)
