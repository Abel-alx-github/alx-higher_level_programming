#!/usr/bin/python3
""" module define rectangle """


class Rectangle():
    """ define rectangle class """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ retrive value of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ set value to width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ retrive value of height """
        return self.__height

    @height.setter
    def height(self, height):
        """ set value to height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
