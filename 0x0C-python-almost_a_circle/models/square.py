#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """initializing Square with Rectangle's instances"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """Setting width to be equal to value hence size"""
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """method that modifies the width and height attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
