#!/usr/bin/python3
""" Define class as square"""


class Square:
    """represent square class"""

    def __init__(self, size=0):
        """initailize the object"""

        self.size = size

    @property
    def size(self):
        """ get the value"""

        return (slef.__size)

    @size.setter
    def size(self, value):
        """ set value, setter """

        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of square"""

        return (self.__size ** 2)

    def my_print(self):
        """print # of square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
