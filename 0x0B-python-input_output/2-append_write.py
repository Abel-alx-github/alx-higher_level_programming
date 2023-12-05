#!/usr/bin/python3
""" module contains function defination"""


def append_write(filename="", text=""):
    """ function that append text to file"""
    with open(filename, mode="a", encoding="utf-8") as a_file:
        b = a_file.tell()
        a_file.write(text)
        return a_file.tell() - b
