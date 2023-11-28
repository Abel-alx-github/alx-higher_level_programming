#!/usr/bin/python3
def magic_string():
    magic_string.ncount = getattr(magic_string, 'ncount', 0) + 1
    return ("BestSchool, " * (magic_string.ncount - 1) + "BestSchool")
