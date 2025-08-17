#!/usr/bin/env python3
"""
Simple line plotting example.
Shows y = x^3 as a solid red line.
"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plot y = x^3 from 0 to 10 as a solid red line.
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    # plot y as a solid red line
    plt.plot(y, 'r-')

    # set x-axis range
    plt.xlim(0, 10)

    # show the graph
    plt.show()
