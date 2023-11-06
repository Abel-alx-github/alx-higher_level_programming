#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in (matrix):
        new_mat = []
        new_mat.append(row)
        for i in new_mat:	       
            print("{:d}".format(i), end="")
