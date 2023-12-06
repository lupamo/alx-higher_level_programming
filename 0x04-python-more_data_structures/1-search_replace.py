#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for index, item in enumerate(my_list):
        if item == search:
            my_list[index] = replace
            return my_list
