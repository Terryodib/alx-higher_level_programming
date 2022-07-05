#!/usr/bin/python3

"""contains a function that appends a string
   at the end of a file
"""


def append_write(filename="", text=""):
    """appends a string to a file
    Args:
        filename: name of the file
        text: text to write into the file
    Return:
        returns the number of characters added
    """
    with open(filename, mode='a', encoding="utf8") as myFile:
        length = myFile.write(text)
    return length
