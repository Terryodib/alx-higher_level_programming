#!/usr/bin/python3

"""contains a function that appends a line
   of text to file
"""


def append_after(filename="", search_string="", new_string=""):
    """appends a string to a file
    Args:
        filename: name of the file
        search_string: the string to insert after
        new_string: the string to insert
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filename, mode='w', encoding='utf-8') as file:
        new_lines = []
        for i in range(len(lines)):
            new_lines.append(lines[i])
            if search_string in lines[i]:
                new_lines.append(new_string)
        file.writelines(new_lines)
