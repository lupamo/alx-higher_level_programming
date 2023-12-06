#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        reversed_str = my_list[::-1]
        for i in reversed_str:
            print("{:d}".format(i))
