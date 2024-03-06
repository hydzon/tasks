"""
Практикум по решению систем линейных уравнений:

Напишите программу, которая будет решать систему линейных уравнений:


"""

import numpy as np
from sys import stdin
import pandas as pd
import matplotlib.pyplot as plt
import re
from scipy.spatial.distance import cosine


def slau_solution():
    tmp_st = [list(map(float, input().split()))]
    for _ in range(len(tmp_st[0]) - 2):
        tmp_st.append(list(map(float, input().split())))
    m1 = np.array(tmp_st)[:, :-1]
    v1 = np.array(tmp_st)[:, -1]
    if np.linalg.det(m1):
        r = np.linalg.solve(m1, v1)
        print(' '.join(list(map(str, r.astype(int)))))
    else:
        print('Система не имеет решений')


def slau_solution2(m, tuple_p):
    m1 = []
    v1 = np.array([])
    for i in range(m):
        x, y = tuple_p[i]
        m1.append([x**i for i in range(m)])
        v1 = np.append(v1, y)
    m1 = np.array(m1)
    if np.linalg.det(m1):
        r = np.linalg.solve(m1, v1)
        return r
    else:
        print('Система не имеет решений')


def f(x, c):
    return c[0] + sum([c[i] * x**i for i in range(1, len(c))])

# ============================================     MAIN     ===========================================================


def main():
    # m1 = [list(map(int, '0 0 0 0 1'.split()))]
    # m1.append(list(map(int, '0 0 0 0 1'.split())))
    # m2 = np.array(m1)
    # m2 = np.append(m2, [list(map(int, '0 0 1 0 1'.split()))], axis=0)
    # m2 = np.concatenate((m2, [list(map(int, '0 0 1 0 1'.split()))]))
    # print(m2[:, :-1])

    c = slau_solution2(6, ((0, 1), (1, 1), (2, 25), (-1, 1), (-2, -23), (0.5, 0.90625)))

    x = np.arange(-1.3, 0.7, 0.01)  # Массив значений аргумента
    plt.plot(x, f(x, c))  # Построение графика
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
