#!/usr/bin/python3
""" module that contain class defination"""


class Student:
    """ defines a student by:
        Public instance attributes:
            first_name, last_name, age
        and Public method
        def to_json(self): that retrieves a dictionary
        representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """ init the new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary of class student instance"""
        if isinstance(attrs, list) and\
                all(type(attr) is str for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        else:
            return self.__dict__
