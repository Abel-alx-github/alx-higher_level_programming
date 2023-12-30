#!/usr/bin/python3
""" define class Square"""


class Square:
    """ represent class of square"""

    def __init__(self, size=0, position=(0, 0)):
        """ initialise Object """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ retrive value of size"""
        return (self.__size)

    @size.setter
    def size(self, value=0):
        """ set value to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ retrive value of position """
        return (self.__position)

    @position.setter
    def position(self, value=0):
        """ set value of position"""
        if not isinstance(value, tuple) or len(value) != 2\
            or not all(isinstance(val, int) for val in value)\
                or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """ print # of self.__size times using position times distanc"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            sep = " "
            for i in range(self.__size):
                print(sep * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """ print format of the class"""
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
        return ("")
