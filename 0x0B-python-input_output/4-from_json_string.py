#!/usr/bin/python3

"""contains a function that returns an object
   represented by a json string
"""

import json


def from_json_string(my_str):
    """returns object representation of a json
    Args:
        my_str: the json
    Return:
        returns the object representation
    """
    return json.loads(my_str)
