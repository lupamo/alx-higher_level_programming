#!/usr/bin/python3
"""
Mylist class inherits from list
Returns a sorted list of int
"""


class MyList(list):
    """instanciating"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """check if list is int"""

        list_sort = sorted(self)
        print(list_sort)
