#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size: The size of the square
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Get or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current area of the square """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size > 0:
            for x in range(self.__size):
                print("#"*self.__size)
        else:
            print()
