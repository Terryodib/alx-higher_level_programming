#!/usr/bin/python3

"""contains a function that writes an object to a text file
   using a json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file
        Args:
            my_obj: the object
            filename: name of the file
        """
    with open(filename, mode='w', encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
