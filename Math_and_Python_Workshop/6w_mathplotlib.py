"""
1) Основы построения графиков

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl


# ============================================     tasks 1-5   =========================================================

def task1():
    # x = np.arange(0, 5, 0.1)
    # y = x**2
    x = range(-10, 10)
    y = [el ** 2 for el in x]
    plt.figure(figsize=(8, 13), dpi=120)
    plt.plot(x, y, 'r')
    plt.xlabel('Аргументы')
    plt.ylabel('Ординаты')
    plt.title('Заголовок')
    # plt.show()
    # plt.savefig('1.png')
    # plt.savefig('1.svg')

    fig = plt.figure()
    axes = fig.add_axes([0, 0, 1, 1])
    axes.plot(x, y, 'r')
    axes2 = fig.add_axes([0.3, 0.5, 0.4, 0.4])
    axes2.plot(x, y, 'g')

    fig, axes = plt.subplots(2, 2)
    axes[0][0].plot(x, y, 'r')
    axes[0][1].plot(x, y, 'g')
    axes[1][0].plot(x, x, 'r')
    axes[1][1].plot(y, y, 'g')
    axes[1][1].set_xlabel('y')
    axes[1][1].set_ylabel('y')
    fig.tight_layout()
    fig.show()


# ============================================     MAIN     ===========================================================

def f(x):
    return x ** 2


def g(x):
    return 1 / x


def h(x):
    return x * np.sin(x)


def main():








if __name__ == '__main__':
    main()
