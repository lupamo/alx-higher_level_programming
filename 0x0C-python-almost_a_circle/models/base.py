#!/usr/bin/python3
"""Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method to return a json string rep"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
