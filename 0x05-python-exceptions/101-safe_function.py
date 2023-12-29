#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    args:
        fct: is a function pointer
        args: argument to fct
    Returns:
        the result otherwise returns None
    """
    try:
        result = fct
        return result
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
