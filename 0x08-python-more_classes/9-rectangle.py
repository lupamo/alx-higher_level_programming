#!/usr/bin/python3
"""A rectangle class with height and width"""


class Rectangle:
    """instanciating a class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        stringer = ""
        for i in range(self.height - 1):
            stringer += str(self.print_symbol) * self.width + '\n'
        stringer += str(self.print_symbol) * self.width
        return stringer

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
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """priints msg when instance is being deleted"""
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """checks if rect is a rectangle instance"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns instance of triangle equal to square"""

        return cls(size, size)
