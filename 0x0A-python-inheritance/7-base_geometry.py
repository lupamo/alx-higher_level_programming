#!/usr/bin/python3


"""
A class BaseGeometry
with an area instance method
"""


class BaseGeometry:
    """pass"""

    def __init__(self):
        pass

    """
    area instance method that raises an exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    """integer_validator method that validates value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

