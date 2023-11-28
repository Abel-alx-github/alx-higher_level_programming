#!/usr/bin/python3
""" define class """


class LockedClass():
    """ represent class Lockedclass"""

    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = None
