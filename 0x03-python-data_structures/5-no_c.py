#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for char in my_string:
        if char not in ["C", "c"]:
            new += char
    return new
