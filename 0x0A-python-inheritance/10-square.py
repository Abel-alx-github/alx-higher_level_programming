#!/usr/bin/python3
""" contain class defination"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ represent inherited class"""

    def __init__(self, size):
        """ init new instance, self"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
