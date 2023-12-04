#!/usr/bin/python3
""" module that contain class defination"""


class MyList(list):
    """ class that inherite from base class list"""
    def __init__(self):
        pass

    def print_sorted(self):
        """ instance methode to print list's containt"""
        a = self.copy()
        a.sort()
        print(a)
