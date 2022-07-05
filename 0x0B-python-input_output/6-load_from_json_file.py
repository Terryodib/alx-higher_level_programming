#!/usr/bin/python3

"""contains a function that creates an
   object from a json file
"""
import json


def load_from_json_file(filename):
    """creates an object from a json file
        Args:
            filename: the name of the file
    """
    with open(filename, mode='r', encoding="utf-8") as myFile:
        my_object = json.load(myFile)
    return my_object
