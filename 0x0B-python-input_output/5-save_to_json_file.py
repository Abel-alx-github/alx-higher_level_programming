#!/usr/bin/python3
""" module that contains function defination"""


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w") as w_file:
        import json
        json.dump(my_obj, w_file)
