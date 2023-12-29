#!/usr/bin/python3
def def safe_print_integer_err(value):
    """ a function that prints an integer.
    args:
        value
    Returns:
        True if value has been correctly printed
        (it means the value is an integer)
        Otherwise, returns False and prints in stderr
        the error precede by Exception:
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
