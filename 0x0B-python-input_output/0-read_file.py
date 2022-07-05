#!/usr/bin/python3

"""reads a text file and prints it to stdout"""


def read_file(filename=""):
    """reads a file and prints its contents
    Args:
        filename: name of the file
    """
    with open(filename, encoding="utf8") as myFile:
        print(myFile.read(), end='')
