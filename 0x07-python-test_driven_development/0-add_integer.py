#!/usr/bin/python3
"""doctest for add function"""
def add_integer(a, b=98):
    """testing a and b
    >>> add_integer(2, 5)
    7
    >>> add_integer(6, -4)
    2
    >>> add_integer(10.5, 6)
    16
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
