#!/usr/bin/env python3
"""
Module provides function to concatenate 2 lists of numbers.
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates 2 lists of integers or floats into a new list

    Args:
        arr1 (List[Number]): The first list of numbers
        arr2 (List[Number]): The second list of numbers

    Returns:
        List[Number]: A new list containing all elements of arr1
                      followed by all elements of arr2

    """
    return arr1 + arr2
