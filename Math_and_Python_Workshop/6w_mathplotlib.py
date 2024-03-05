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

    x = np.arange(0.1, 5, 0.1)
    fig, axis = plt.subplots(figsize=(8, 10))
    axis.plot(x, f(x), x, g(x))
    axis.plot(x, h(x))
    axis.legend(['F(x)', 'G(x)', 'H(x)'])
    fig.show()


# ============================================     MAIN     ===========================================================

def f(x, a, b):
    try:
        return (x ** b + a ** b) / x ** b
    except Exception:
        print('ops')


def g(x):
    return 1 / x


def h(x):
    return x * np.sin(x)


def main():

    xm = np.arange(-5, -0.01, 0.1)
    xb = np.arange(0.01, 5, 0.1)
    x = np.arange(-5, 5, 0.05).round(3)
    fig, axis = plt.subplots(figsize=(8, 8))
    axis.plot(x, f(x, 1, 1), 'r')
    axis.plot(x, f(x, 2, 1), 'b')
    axis.plot(x, f(x, 1, 2), 'g')
    axis.legend(['α=1,β=1', 'α=2,β=1', 'α=1,β=2'])
    axis.set_ylim([-30, 30])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('$f(x) = (x^a + a^b) / x^b$')
    fig.tight_layout()
    fig.show()


if __name__ == '__main__':
    main()
