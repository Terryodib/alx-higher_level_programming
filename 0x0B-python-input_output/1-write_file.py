#!/usr/bin/python3

"""contains a function that writes a string to a
   text file and returns the number of characters
   written
"""


def write_file(filename="", text=""):
    """write a text file
    Args:
        filename: name of the file
        text: text to write into the file
    Return:
        returns the number of characters written
    """
    with open(filename, mode='w', encoding="utf8") as myFile:
        length = myFile.write(text)
    return length
