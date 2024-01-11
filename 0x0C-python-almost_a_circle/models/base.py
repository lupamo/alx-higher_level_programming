#!/usr/bin/python3
"""Base class"""


class Base():
    """
    This class will be the base class
    of other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instanciating the Base class
        Args:
        id = None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
