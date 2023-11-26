#!/usr/bin/python3
""" define a function """


def matrix_divided(matrix, div):
    """ function that divided list of list"""

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
