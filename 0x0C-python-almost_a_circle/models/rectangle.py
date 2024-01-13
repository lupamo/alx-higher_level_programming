#!/usr/bin/python3


"""
Rectengle class which inherits from Base
"""


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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Allows us to define width which is called
        when getting, setting or deleting the value of the property
        """

        return self.__width

    @width.setter
    def width(self, value):
        """method that modifies the width attribute"""

        if not isinstance(value, int):
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

        if not isinstance(value, int):
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
        if not value < 0:
            raise TypeError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """allows y to access special methods
            getter, setter and deleter methods)"""

        return self.__y

    @y.setter
    def y(self, value):
        """modifies our private x attribute
        value: the value which x attribute is to be set to
        """
        if value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value
