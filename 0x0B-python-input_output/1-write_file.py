#!/usr/bin/python3
""" module contains function defination"""


def write_file(filename="", text=""):
    """ function that write to file and return number of bytes written"""

    with open(filename, mode="w", encoding="utf-8") as w_file:
        w_file.write(text)
        return w_file.tell()
