#!/usr/bin/python3
"""Base class"""
import json
import os
import csv


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
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """it returns an instance with all attributes already set"""
        if "size" in dictionary:
            dummy_instance = cls(1)
        else:
            dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    def update(self, *args, **kwargs):
        """üpdates arg value with args or kwargs"""
        if args:
            arg = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, arg[i], value)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    @classmethod
    def load_from_file(cls):
        """Ït returns a list of instances"""
        file_name = "{}.json".format(cls.__name__)
        instance_lst = []
        try:
            with open(file_name, mode='r+', encoding='UTF-8') as file:
                json_str = file.read()
            obj_dict = cls.from_json_string(json_str)
            for i in obj_dict:
                instance_lst += [cls.create(**i)]
        except FileNotFoundError:
            pass
        return instance_lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """"Seralizing and saving instances of CSV file."""
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, 'w', newline='') as file:
            written = csv.writer(file)
            for obj in list_objs:
                written.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        file_name = "{}.csv".format(cls.__name__)
        instance_lst = []
        try:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    obj_dict = dict(zip(cls.create().to_dictionary().keys(),
                                        map(int, row)))
                    instance_lst.append(cls.create(**obj_dict))
        except FileNotFoundError:
            pass
        return instance_lst
