"""
1)  Вектор A содержит float числа как больше, так и меньше нуля.
Округлите их до целых и результат запишите в переменную Z. Округление должно быть "от нуля", т.е.:
- положительные числа округляем всегда вверх до целого
- отрицательные числа округляем всегда вниз до целого
- 0 остаётся 0

2)  Даны 2 вектора целых чисел A и B.
Найдите числа, встречающиеся в обоих векторах и составьте их по возрастанию в вектор Z.
Если пересечений нет, то вектор Z будет пустым.


3)  На вход подаётся 2 строки:
1-я строка содержит 2 натуральных числа: n, m
2-я строка содержит число k

    Создайте матрицу a размера n*m такую, что каждая её строка содержит числа от k до k+m-1 (с шагом 1).

    Создайте матрицу b размера n*m такую, что каждый её столбец содержит числа от k до k+n-1 (с шагом 1).


"""

import datetime
from functools import reduce
import numpy as np


# ============================================     tasks 1-5   =========================================================


def task1(z):
    # z[z < 0], z[z > 0] = np.floor(z[z < 0]), np.ceil(z[z > 0])
    z = np.where(z > 0, np.ceil(z), np.floor(z))
    return z


def task2(a, b):
    return np.intersect1d(a,  b)


def task3(n, m, k):
    a = np.zeros((n, m), dtype='float') + np.arange(k, m + 1)[:m]
    b = np.zeros((n, m), dtype='float') + np.arange(k, n + 1)[:n].reshape(n, 1)
    return print(f'{a} \n\n {b}')

# ============================================     MAIN     ===========================================================


def main():

    # print(task1(np.array([9.8, 0, -1.2, 0])))
    # print(task2(np.array([0, 9, 7, 1, 3, 7, 5, 2, 5, 1]), np.array([3, 1, 3, 7, 4, 1, 8, 1, 1, 8])))
    # print(np.arange(np.datetime64('2016-07'), np.datetime64('2016-08'), dtype='datetime64[D]'))
    # print(np.arange(np.datetime64('2016-07', 'D'), np.datetime64('2016-08', 'D'), dtype=np.datetime64))
    # task3(5, 4, -5)
    # print(np.fromiter(range(10), dtype='float'))
    # print(np.around(np.linspace(0, 1, 10, endpoint=False), decimals=3)[1:])
    print(np.geomspace(1, 256, 9))




if __name__ == '__main__':
    main()
