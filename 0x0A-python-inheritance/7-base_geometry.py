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
        """Raise exception"""
        raise Exception("area() is not implemented")

    """integer_validator method that validates value"""
    def integer_validator(self, name, value):
        """
        checks if value is appropriate
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
