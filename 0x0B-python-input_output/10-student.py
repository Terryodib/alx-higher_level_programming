#!/usr/bin/python3
"""contains a class"""


class Student:
    """student class"""

    def __int__(self, first_name, last_name, age):
        """initialization of student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves  a dictionary representation of
           a student instance
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except TypeError:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
