#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    mul_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return mul_matrix
