#!/usr/bin/python3


"""
A class BaseGeometry
with an area instance method
"""


class BaseGeometry:
    """
    area instance method that raises an exception
    """

    def area(self):
        """Raise exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        checks if value is appropriate
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
