#!/usr/bin/python3
"""Define class as square"""


class Square:
    """ represent square class, statment"""

    def __init__(self, size):
        """ initailize the object"""
        self.size = size

    @property
    def size(self):
        """ Args:
            size(int): method to retrive value
        Return: returns value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Args:
            size(int): method to set value, setter
            """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Args:
            self: object
            Return: area of square"""
        return (self.__size * self.__size)
