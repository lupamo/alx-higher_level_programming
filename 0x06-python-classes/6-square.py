#!/usr/bin/python3
""""class with a method"""


class Square:
    """initializing self"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    """private position instance property"""

    @property
    def position(self):
        return self.__position

    """position setter"""

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """area method instance"""

    def area(self):
        return (self.__size**2)

    """prints out # stdout area"""

    def my_print(self):
        if self.__size != 0:
            for liner in range(self.__position[1]):
                print("", end="\n")
            for j in range(self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
        else:
            print()


"""exception, setter and area found at class"""
