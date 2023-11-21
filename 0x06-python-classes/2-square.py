#!/usr/bin/python3

""" Define class named as square"""


class Square:
    """block of this class, statment"""
    def __init__(self, size=0):
        """ initialize the instance or object of this class.
        Args:
            size(int): size of new instance."""
        if size < 0:
            raise ValueError('size must be >= 0')
        elif not isinstance(size, int):
            raise TypeError('size must be an integer')
        self._size = size
