#!/usr/bin/python3
"""
    returns the dictionary description with simple data structure
    for JSON serialization of an object:
"""


def class_to_json(obj):
    """returns the dictionary description"""
    if not hasattr(obj, "__dict__"):
        return obj
    dictt = {}
    for key, value in obj.__dict__.items():
        if isinstance(key, (dict, str, bool, int, float, list)):
            dictt[key] = value
        elif isinstance(key, (tuple, set)):
            dictt[str(key)] = value
        elif hasattr(value, "__dict__"):
            dictt[key] = class_to_json(value)
    return dictt
