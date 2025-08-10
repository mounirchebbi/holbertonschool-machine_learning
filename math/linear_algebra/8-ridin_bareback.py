#!/usr/bin/env python3
"""
Module / function to perform matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication between two 2D matrices.

    Args:
        mat1: The first 2D matrix (list of lists of ints/floats).
        mat2: The second 2D matrix (list of lists of ints/floats).

    Returns:
        A new 2D matrix that is the result of mat1 x mat2,
        None if the matrices cannot be multiplied.
    """
    # Check if multiplication is possible: cols in mat1 == rows in mat2
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize result matrix with zeros
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            # Compute dot product for cell (i, j)
            dot_product = 0
            for k in range(len(mat1[0])):
                dot_product += mat1[i][k] * mat2[k][j]
            row.append(dot_product)
        result.append(row)

    return result
