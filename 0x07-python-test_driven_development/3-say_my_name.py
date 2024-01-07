#!/usr/bin/python3

"""
Say_name function
first_name must be a string
last_name must be a string
return My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):

    """
    checks if first_name is string
    also checks if last_name is a str
    prints a string containing first_name & last_name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
