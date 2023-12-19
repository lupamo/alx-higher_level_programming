#!/usr/bin/python3
""""class with a method"""


class Square:
    """initializing self"""

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """private instance"""

    @property
    def size(self):
        return (self.__size)

    """using getter"""
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """area method instance"""

    def area(self):
        return (self.__size**2)


"""exception, setter and area found at class"""
