#!/usr/bin/env python3
"""
Histogram example.
Shows distribution of student grades for Project A.
"""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Plot a histogram of student grades with bins of 10.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # histogram with bins every 10 from 0 to 100, black edges
    plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor="black")

    # labels and title
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")

    # show plot
    plt.show()
