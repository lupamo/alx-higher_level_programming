#!/usr/bin/python3
"""
A funcion that writes an object to a
text file
"""

import json


def save_to_json_file(my_obj, filename):
    """the object will be saved to file"""

    file_f = json.dumps(my_obj)
    with open(filename, 'w+', encoding='utf-8') as f:
        return f.write(file_f)
