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

    def area(self):
        """ return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        rect_description = "[" + str(self.__class__.__name__) + "] "
        rect_description += str(self.__width) + "/" + str(self.__height)
        return rect_description
