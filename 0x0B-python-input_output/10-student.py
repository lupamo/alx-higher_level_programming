#!/usr/bin/python3
"""
A class that defines a student
"""


class Student():
    """initializing the class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """turns a dictionary of student instance"""
        new_dict = {}
        new_dict = self.__dict__
        if attrs is None:
            return new_dict
        for key, value in new_dict.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
