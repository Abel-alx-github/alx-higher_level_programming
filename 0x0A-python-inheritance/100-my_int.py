#!/usr/bin/python3
""" define class"""


class MyInt(int):
    """represent inherited class from int"""
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return super().__eq__(other)
