#!/usr/bin/python3

"""
Module 0-pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of integers
    +representing Pascal's triangle
    """
    if n <= 0:
        return []
    # [1] is the initial element
    triangle = [[1]]

    # iterate to up size n - 1
    for i in range(n - 1):
        # pick the previous list
        temp = [0] + triangle[-1] + [0]
        # create a new row
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
            triangle.append(row)
    return triangle
