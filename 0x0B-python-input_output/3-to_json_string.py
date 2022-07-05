#!/usr/bin/python3

"""contains a function that returns the json
   representation of an object
"""
import json


def to_json_string(my_obj):
    """returns json representation of an object
    Args:
        my_obj: the object
    Return:
        returns the json representation
    """
    return json.dumps(my_obj)
