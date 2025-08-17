#!/usr/bin/env python3
"""
Exponential decay example.
Plots decay of Carbon-14 over time.
"""

import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    Plot exponential decay of C-14 with a log-scaled y-axis.
    """
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))

    # plot line
    plt.plot(x, y)

    # labels and title
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of C-14")

    # set y-axis log scale
    plt.yscale("log")

    # set x-axis range
    plt.xlim(0, 28650)

    # show plot
    plt.show()
