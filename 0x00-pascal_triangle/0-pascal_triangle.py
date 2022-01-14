# The function a list of integers representing the Pascal's triangle of n

from math import factorial 

def pascal_triangle (n):
    """
    Calculate pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range (n):
            tmp = []
            for j in range (i+1):
                value = int(factorial(i)/ (factorial(j) * factorial(i - j)))
                tmp.append(value)
               
            triangle.append(tmp)
    return triangle
