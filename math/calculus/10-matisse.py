#!/usr/bin/env python3
""" Module to calculate dreiv of polynom"""


def poly_derivative(poly):
    """Return the derivative of a polynomial represented as a list of coefficients."""
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None
    if len(poly) == 1:  # derivative of a constant
        return [0]
    # Multiply each coefficient by its power and skip the constant term
    derivative = [i * poly[i] for i in range(1, len(poly))]
    return derivative if derivative else [0]
