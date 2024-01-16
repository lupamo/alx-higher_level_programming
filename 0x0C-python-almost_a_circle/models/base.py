#!/usr/bin/python3
"""Base class"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_n = "{}.json".format(cls.__name__)
        objs_lst = []

        if list_objs is not None:
            for i in list_objs:
                objs_lst += [i.to_dictionary()]

        json_str = Base.to_json_string(objs_lst)
        with open(file_n, mode='w+', encoding="UTF-8") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            json_string = []
        return json.loads(json_string)
