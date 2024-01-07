#!/usr/bin/python3
"""
function matrix_divided(matrix, div):
doctest for the function
returns matrix items divided by div
"""

def matrix_divided(matrix, div):

    """
    looking for all possible test cases
    on matrix: size, int or float
    on div: int or float or > 0
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError()
    for items in matrix[1:]:
        if len(items) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
