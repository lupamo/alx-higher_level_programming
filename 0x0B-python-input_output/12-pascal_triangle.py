#!/usr/bin/python3
"""
a function that returns a list of ints
representing pascal triangle
Technical interview
"""


def pascal_triangle(n):
    """
    pascal triangle of size n
    returns a triangle
    """
    if n <= 0:
        return []
    p_triangle = [[1]]

    while len(p_triangle) != n:
        trio = p_triangle[- 1]
        temp = [1]
        for j in range(len(trio) - 1):
            temp.append(trio[j] + trio[j + 1])
        temp.append(1)
        p_triangle.append(temp)
    return p_triangle
