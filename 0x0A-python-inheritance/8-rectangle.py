#!/usr/bin/python3
""" module that contain class defination """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ represent inherited class"""

    def __init__(self, width, height):
        """ init the instance slef"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
