#!/usr/bin/python3

"""Rectangle Class."""

class Rectangle:
    """Defines the blueprint of a rectangle."""
    def __init__(self, width=0, height=0):
        """An object constructor method."""

        self.__width = width
        self.__height = height
    def __str__(self):
        """Returns an informal and nicely printable string representation"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message for del"""

        print("Bye rectangle...")

    @property
    def width(self):
        """Gets the width private attribute value."""

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
         """Sets the height private attribute value."""
         if not isinstance(value, int):
             raise TypeError("height must be an integer")
         if value < 0:
             raise ValueError("height must be >= 0")
         self.__height = value

    def area(self):
        """A public object method."""

        return self.__width * self.__height

    def perimeter(self):
        """A public object method."""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)


