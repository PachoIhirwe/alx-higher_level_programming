#!/usr/bin/python3

class Square:
    """represent"""
    def __init__(self, size=0):
        """intilaizes Args"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
        def area(sefl):
            """return"""
            return (self.__size * self.__size)
