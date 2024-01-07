#!/usr/bin/python3
"""doctest for add function
    checks if a is an integer or float
    checks if b is also an integer or a float
    Return: a + b
"""


def add_integer(a, b=98):

    """testing a and b
    if a or b are not an int or float raise error
    """

    if not isinstance(a, (int, float)):

        """Raising an Error when a is not integer or float"""

        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):

        """Raising an Error whan b is not an int or float"""

        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
