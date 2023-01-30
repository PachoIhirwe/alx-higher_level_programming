#!/usr/bin/python3
"""Rectangle Class."""

class Rectangle:
    """Defines the blueprint of a rectangle"""
    def __init__(self, width=0, height=0):
         """An object constructor method."""
         self.__width = width
         self.__height = height

    @property
    def width(self):
       """Gets the width private attribute value"""

       return self.__width

    @width.setter
    def width(self, value):
         """Sets the width private attribute value."""
         if not isinstance(value, int):
             raise TypeError("width must be an integer")
         if value < 0:
             raise ValueError("width must be >= 0")

         self.__width = value


    @property
    def height(self):
        """Gets the height private attribute value."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height private attribute value."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
