#!/usr/bin/python3
"""contain function defination"""


def pascal_triangle(n):
    """
    that returns a list of lists of integers
    representing the Pascal’s triangle
    """
    if n <= 0:
        a = []
        return a
    if n == 1:
        a = [[1]]
        return a
    elif n == 2:
        a = [[1], [1, 1]]
        return a
    elif n > 2:
        no_row = n - 2
        a = [[1], [1, 1]]
        while no_row > 0:
            len_a = len(a)
            b = a[len_a - 1]
            len_b = len(b)
            new = [1]
            for i in range(len_b - 1):
                new.append(b[i] + b[i+1])
            new.append(1)
            a.append(new)
            no_row -= 1
        return a
