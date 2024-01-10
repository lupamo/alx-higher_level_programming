#!/usr/bin/python3

"""
inheritance from Base Geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited BaseGeometry"""

    def __init__(self, width, height):
        """instatiating width an height"""

        super().integer_validator("width", width)
        self._width = width
        super().integer_validator("height", height)
        self._height = height

    def area(self):
        """returns area of a rectangle"""

        return self._width * self._height

    def __str__(self):
        """string representation of rectangle"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self._width) + "/" + str(self._height)
        return string
