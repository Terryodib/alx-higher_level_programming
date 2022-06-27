#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """initializes the instance object
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the value of the width
        Returns:
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """method that defines the width
        Args:
            value: width of the rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of the height
        Returns:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """method that defines the height
        Args:
            value: height of the rectangle
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that returns the area of the rectangle
        Returns:
            area
        """
        return self.width * self.height

    def perimeter(self):
        """method that returns the perimeter of rectangle
        Returns:
            perimetr
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height
