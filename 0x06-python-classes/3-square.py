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

    def area(self):
        """Returns the current area of the square """
        return self.__size * self.__size
