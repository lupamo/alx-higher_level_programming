#!/usr/bin/python3
"""
if obj isinstance of a_class
return true
"""


def is_kind_of_class(obj, a_class):
    """return true if obj isinstance of a_class
    or it's subclass
    """

    if isinstance(obj, a_class):
        return True
    else:
        False
