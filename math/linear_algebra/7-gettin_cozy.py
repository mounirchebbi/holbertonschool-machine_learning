#!/usr/bin/env python3
"""
Module / function to concatenate 2 2d matrices along a given axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a given axis

    Args:
        mat1: The first 2D matrix (list of lists of ints/floats)
        mat2: The second 2D matrix (list of lists of ints/floats)
        axis: The axis along which to concatenate (0 for rows, 1 for columns)

    Returns:
        A new 2D matrix containing the concatenation result
        None if the matrices cannot be concatenated
    """
    # Deep copy to avoid modifying originals
    if axis == 0:
        # Check column count
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    elif axis == 1:
        # Check row count
        if len(mat1) != len(mat2):
            return None
        return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]

    return None
