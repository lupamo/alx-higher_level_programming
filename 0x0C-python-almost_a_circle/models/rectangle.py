#!/usr/bin/python3
"""Rectangle class which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Base inherited by Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instaciating rectangle
        Args
        width: private instance attribute
        height: private instance attribute
        x: private instance
        y: private instance
        id:inherited instance
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """Improving rectangle with x & y"""
        print("\n"*self.x, end="")
        for row in range(self.height):
            print(" "*self.x + "#"*self.width)

    def __str__(self):
        """Overiding The __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updating rectangle with args"""
        attr = ["id", "size", "x", "y"]

        for i, value in enumerate(args):
            if i > (len(attr) - 1):
                break
            setattr(self, attr[i], value)
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """"
        returns area by multiplying width and height
        Area method which returns area of a rectangle
        """
        return self.width * self.height

    @property
    def width(self):
        """Allows us to define width which is called
        when getting, setting or deleting the value of the property
        """

        return self.__width

    @width.setter
    def width(self, value):
        """method that modifies the width attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Allows us to define height which is called
        when getting, setting or deleting the value of the property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """method that modifies the height attribute"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """it allows x access special methods(getter, setter and deleter)"""

        return self.__x

    @x.setter
    def x(self, value):
        """modifies our private x attribute
        value: the value which x attribute is to be set to
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """allows y to access special methods
            getter, setter and deleter methods)"""

        return self.__y

    @y.setter
    def y(self, value):
        """modifies our private y attribute
        value: the value which y attribute is to be set to
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
