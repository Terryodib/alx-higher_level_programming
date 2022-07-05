#!/usr/bin/python3

"""contains a function that returns
   the dictionary description with simple
   data structure for json serialization
   of an object
"""


def class_to_json(obj):
    """returns a dictionary representation of obj
        Args:
            obj: the object
    """
    return obj.__dict__
