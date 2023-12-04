#!/usr/bin/python3
""" contains class defination"""


class BaseGeometry:
    """ represent an empty class """
    def __init__(self):
        pass

    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """  validates value """
        if isinstance(name, str):
            self.name = name
        if not (isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
