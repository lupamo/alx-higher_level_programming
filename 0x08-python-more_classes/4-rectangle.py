#!/usr/bin/python3
"""A rectangle class with height and width"""


class Rectangle:
    """instanciating a class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width property"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """prints a rectangle using #"""

        if self.width == 0 or self.height == 0:
            return ""
        str = ""
        for i in range(self.height - 1):
            str += "#" * self.width + '\n'
        str += "#" * self.width
        return str

    def area(self):
        """returns the area of the triangle"""

        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return (2*(self.width+self.height))

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f"Rectangle(width={self.width}, height={self.height})"
