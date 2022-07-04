#!/usr/bin/python3

"""contains a lookup function"""


def lookup(obj):
    """method that returns the list of available attributes and methods
    of an object
    Returns:
        a lists object
    """
    return dir(obj)
