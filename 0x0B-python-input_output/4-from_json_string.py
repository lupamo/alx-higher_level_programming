#!/usr/bin/python3
"""
function returns an object represented
by JSON string
"""


import json


def from_json_string(my_str):
    """Returns an obect"""

    obj_str = json.loads(my_str)
    return obj_str
