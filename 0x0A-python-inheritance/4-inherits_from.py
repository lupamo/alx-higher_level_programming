#!/usr/bin/python3
"""
inherits_from returns true if
object is instance of a class
either directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    checks if instance is directly or
    indirectly inherited by a class
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
