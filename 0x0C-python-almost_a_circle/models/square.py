#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """initializing Square with Rectangle's instances"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """returns a dictionary representation of a square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """updates square with args and kwargs"""
        args_attr = ["id", "size", "x", "y"]

        for i, value in enumerate(args):
            if i > (len(args_attr) - 1):
                break
            setattr(self, args_attr[i], value)
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """Setting width to be equal to value hence size"""
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """method that modifies the width and height attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overiding The __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
