#!/usr/bin/python3

"""
print_square(size) function
prints a square with #
retruns a square with size length
"""


def print_square(size):

    """
    checks if size is an int
    checks if size > 0
    checks if size is a float
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        hash_l = "#" * size
        print(hash_l)
