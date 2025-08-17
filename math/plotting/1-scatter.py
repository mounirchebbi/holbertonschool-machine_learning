#!/usr/bin/env python3
"""
Scatter plot example.
Shows men's height vs weight.
"""

import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """
    Plot men's height vs weight as magenta scatter points.
    """
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    # scatter plot with magenta points
    plt.scatter(x, y, c='m')

    # axis labels and title
    plt.xlabel("Height (in)")
    plt.ylabel("Weight (lbs)")
    plt.title("Men's Height vs Weight")

    # show plot
    plt.show()
