#!/usr/bin/python3
"""
A function that returns a JSON
representation of string
"""


import json


def to_json_string(my_obj):
    """Returns a JSON representation"""

    json_rep = json.dumps(my_obj)
    return json_rep
