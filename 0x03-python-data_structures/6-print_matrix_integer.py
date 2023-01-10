#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ My a function that prints a matrix of integers."""
    for row in matrix:
        for column in row:
            if column == row[-1]:
                print("{}".format(column), end='')
            else:
                print("{}".format(column), end=' ')
        print()
