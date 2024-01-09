#!/usr/bin/python3
"""
a function that inserts a line
of text to a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """check and inserts a text to the string"""

    with open(filename, "r+") as f:
        line_text = ""
        for line in f:
            if search_string in line:
                line += new_string
            line_text += line
        f.seek(0)
        f.write(line_text)
