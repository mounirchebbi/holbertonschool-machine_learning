#!/usr/bin/env python3
def matrix_shape(matrix):
    """
    Returns the dimensions of a matrix as a list of integers.

    Args:
        matrix (list): A multi-dimensional list.

    Returns:
        list: Sizes of the matrix in each dimension.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
