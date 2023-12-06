#!/usr/bin/python3
""" contain function defination"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after
    each line containing a specific string
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        new = ""
        for line in f:
            new += line
            if line.find(search_string) != -1:
                new += new_string
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(new)
