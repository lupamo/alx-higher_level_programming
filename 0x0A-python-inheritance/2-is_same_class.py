#!/usr/bin/python3
"""
is_same_class function checks if
obj is instance of class
return True
"""


def is_same_class(obj, a_class):
    """checks if obj type is equal a_class"""

    if type(obj) is a_class:
        return True
    else:
        return False
