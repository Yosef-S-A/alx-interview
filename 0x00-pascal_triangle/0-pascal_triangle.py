#!/usr/bin/python3

# The function a list of integers representing the Pascal's triangle of n

def pascal_triangle (n):
    """
    Calculate pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range (n):
            j = 11 ** i
            triangle.append(list(str(j)))
    return triangle
