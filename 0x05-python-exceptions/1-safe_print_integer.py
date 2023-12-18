#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value.isdigit():
            print("{:d}".format(value))
            return True
        else:
            return False
    except AttributeError:
        return False
