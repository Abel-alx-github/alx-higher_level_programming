#!/usr/bin/python3
""" contains class defination"""


class BaseGeometry:
    """ represent an empty class """
    def __init__(self):
        pass

    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")
