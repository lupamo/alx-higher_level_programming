#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = None
    key_top = None
    if a_dictionary:
        for key, val in a_dictionary.items():
            if biggest is None or val > biggest:
                biggest = val
                key_top = key
    return key_top
