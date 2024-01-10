#!/usr/bin/python3

"""
adds an attribute to an object
"""


def add_attribute(obj, attr, val):
    """checks if obj has attr if not it adds the val"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
