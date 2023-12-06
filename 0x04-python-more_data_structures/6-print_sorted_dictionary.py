#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_sort = sorted(a_dictionary.keys())
    for i in key_sort:
        val = a_dictionary[i]
        print("{}: {}".format(i, val))
