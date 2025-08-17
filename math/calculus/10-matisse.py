#!/usr/bin/env python3
""" Module to calculate dreiv of polynom"""


def poly_derivative(poly):
    """Return the derivative of a polynomial represented as a list of coefficients."""
    # Validate input
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None

    # Derivative of a constant
    if len(poly) == 1:
        return [0]

    # Compute derivative: skip constant term, multiply by power
    derivative = [i * poly[i] for i in range(1, len(poly))]

    return derivative if derivative else [0]
