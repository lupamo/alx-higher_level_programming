#!/usr/bin/python3
"""
A funcion that writes an object to a
text file
"""

import json


def save_to_json_file(my_obj, filename):
    """the object will be saved to file"""

    with open(f"{filename}", 'w') as f:
        return json.dumps(my_obj)
