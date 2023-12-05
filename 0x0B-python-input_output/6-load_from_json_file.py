#!/usr/bin/python3
""" module contains function defination """


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file"""
    import json
    with open(filename, "r") as r_jfile:
        return json.load(r_jfile)
