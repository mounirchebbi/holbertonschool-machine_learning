#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Plot a stacked bar graph of fruit counts per person"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))  # 4 fruits x 3 people
    people = ['Farrah', 'Fred', 'Felicia']
    fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

    plt.figure(figsize=(6.4, 4.8))
    bottoms = np.zeros(fruit.shape[1])

    for i in range(fruit.shape[0]):
        plt.bar(people, fruit[i], bottom=bottoms, color=colors[i], width=0.5, label=fruits[i])
        bottoms += fruit[i]

    plt.ylabel("Quantity of Fruit", fontsize='x-small')
    plt.yticks(np.arange(0, 81, 10), fontsize='x-small')
    plt.ylim(0, 80)
    plt.xlabel("", fontsize='x-small')  # ensures no label misalignment
    plt.title("Number of Fruit per Person", fontsize='x-small')
    plt.legend(fontsize='x-small')
    plt.show()
