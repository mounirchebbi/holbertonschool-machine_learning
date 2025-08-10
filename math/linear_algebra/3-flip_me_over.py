#!/usr/bin/env python3
"""
Module for transposing a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Calculate the transpose of a 2D matrix.

    Args:
        matrix (list of lists): The matrix to transpose.

    Returns:
        list of lists: A new matrix representing the transpose.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
