#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Plot a stacked bar graph of fruit counts per person"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))  # 4 fruits x 3 people
    people = ['Farrah', 'Fred', 'Felicia']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']  # apples, bananas, oranges, peaches
    fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']

    # Bottom positions for stacking
    bottoms = np.zeros(fruit.shape[1])

    plt.figure(figsize=(6.4, 4.8))

    for i in range(fruit.shape[0]):  # Loop through each fruit
        plt.bar(people, fruit[i], bottom=bottoms, color=colors[i], width=0.5, label=fruits[i])
        bottoms += fruit[i]  # Update bottom for next fruit

    plt.ylabel("Quantity of Fruit")
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title("Number of Fruit per Person")
    plt.legend()
    plt.show()
