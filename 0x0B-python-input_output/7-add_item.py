#!/usr/bin/python3
"""a script that adds all arguments to a Python list
and then save them to a file:"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_n = "add_item.json"
with open(file_n, 'a', encoding="utf-8") as f:
    try:
        list_my = load_from_json_file(file_n)
    except Exception:
        list_my = []
    for arg in range(1, len(argv)):
        list_my += [argv[arg]]
    save_to_json_file(list_my, file_n)
