#!/usr/bin/python3
"""contains a class"""


class Student:
    """student class"""

    def __int__(self, first_name, last_name, age):
        """initialization of student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a
           student class
        """
        return self.__dict__
