#!/usr/bin/python3
"""
A functon that finds peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """list integers reversed"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
