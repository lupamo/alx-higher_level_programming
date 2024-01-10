#!/usr/bin/python3

"""
inheritance from Base Geometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class which Inherited BaseGeometry"""

    def __init__(self, size):
        """instatiating width an height"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size
