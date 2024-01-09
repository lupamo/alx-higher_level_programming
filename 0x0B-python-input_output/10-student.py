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

        """
        retrives  dictionary of student instance
        If attrs is a list of strings, only attribute names contained in this list must be retrieved
        """
        new_dict = self.__dict__
        if type(attrs) is list and all(type(element)
                                       is str for element in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return new_dict
