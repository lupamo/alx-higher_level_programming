#!/usr/bin/python3

"""
inheritance from Base Geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited BaseGeometry"""

    def __init__(self, width, height):
        """instatiating width an height"""

        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
