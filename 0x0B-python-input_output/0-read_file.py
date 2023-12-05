#!/usr/bin/python3
""" a module contanins function defination"""


def read_file(filename=""):
    """ define function that read and print containt of file"""
    with open(filename, mode="r", encoding="utf-8") as r_file:
        for line in r_file:
            print(line, end="")
