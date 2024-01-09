#!/usr/bin/python3
"""
A class that defines a student
"""


class Student:
    """initializing the class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """turns a dictionary of student instance"""

        return self.__dict__
