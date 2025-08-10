#!/usr/bin/env python3
"""
Module for adding two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Add two 2D matrices element-wise

    Args:
        mat1 (list of lists): First matrix (ints/floats)
        mat2 (list of lists): Second matrix (ints/floats)

    Returns:
        list of lists: New matrix with element-wise sums, or None if shapes differ
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
