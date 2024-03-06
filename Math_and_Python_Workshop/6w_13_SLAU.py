"""
Практикум по решению систем линейных уравнений:

Напишите программу, которая будет решать систему линейных уравнений:


"""

import numpy as np
from sys import stdin
import pandas as pd
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


# ============================================     MAIN     ===========================================================


def main():
    # m1 = [list(map(int, '0 0 0 0 1'.split()))]
    # m1.append(list(map(int, '0 0 0 0 1'.split())))
    # m2 = np.array(m1)
    # m2 = np.append(m2, [list(map(int, '0 0 1 0 1'.split()))], axis=0)
    # m2 = np.concatenate((m2, [list(map(int, '0 0 1 0 1'.split()))]))
    # print(m2[:, :-1])

    slau_solution()


if __name__ == '__main__':
    main()
