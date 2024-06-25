#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

'''all the lesson from month 0 to month 8 are rquired'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    if n <= 0:
        return []
    triangle = [[1]*(k+1) for k in range(n)]
    for k in range(n):
        for l in range(1, k):
            triangle[k][l] = triangle[k-1][l-1] + triangle[k-1][l]
    return triangle
