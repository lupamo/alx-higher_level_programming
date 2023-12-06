#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_comp = ["{}: {}".format(
        key, value) for key, value in a_dictionary.items()]
    print("\n".join(dic_comp))
