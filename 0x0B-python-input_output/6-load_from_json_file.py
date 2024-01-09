#!/usr/bin/python3
"""
A funcion that creates an object from
JSON file
"""

import json


def load_from_json_file(filename):
    """the object will be created from json data"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
