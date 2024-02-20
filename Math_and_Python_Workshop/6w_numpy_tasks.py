"""
1) На вход подаётся 2 набора целых чисел (они представляют из себя вектора равной длины,
т.е. с одинаковым количеством элементов).
Используя векторные операции создайте и сохраните:
в переменную V1 Numpy вектор с числами из 1 строки
в переменную V2 Numpy вектор с числами из 2 строки
в переменную V3 Numpy вектор с покоординатными суммами V1 и V2
в переменную V4 Numpy вектор с покоординатными произведениями каждого второго числа V1 на каждое второе число V2,
развёрнутого в обратном порядке

2) На вход подаётся 2 набора целых чисел.
Создайте вектор V такой, что он будет содержать числа из 1 набора, делящиеся нацело на предпоследнее число
из 2 набора и разделённые на это число.
Если таких чисел не найдётся, то вектор V будет пустым (т.е. не будет содержать элементов).


3) В этой задаче нам даны 3 переменные: A1, A2, A3. Каждая содержит вектор с 2 координатами
соответствующей вершины треугольника.
Найдите площадь треугольника и выведите её на печать. (по формуле Герона)



"""

import numpy as np
import datetime

# ============================================     tasks 1-5   =========================================================


def task1(v1, v2):
    v1 = np.array(v1.split(','), dtype=int)
    v2 = np.array(v2.split(','), dtype=int)
    v3 = v1 + v2
    v4 = v1[::2] * v2[::-2]
    print(v1, v2, v3, v4)


def task2(v1, v2):
    v1 = np.array(v1.split(','), dtype=float)
    v2 = np.array(v2.split(','), dtype=float)
    return v1[v1 % v2[-2] == 0] / v2[-2]


def task3(v1, v2, v3):
    # a = ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** 0.5
    a = np.linalg.norm(v1 - v2)
    # b = ((v2[0] - v3[0]) ** 2 + (v2[1] - v3[1]) ** 2) ** 0.5
    b = np.linalg.norm(v1 - v3)
    # c = ((v3[0] - v1[0]) ** 2 + (v3[1] - v1[1]) ** 2) ** 0.5
    c = np.linalg.norm(v2 - v3)
    p = (a + b + c) / 2
    return (p*(p - a)*(p - b)*(p - c)) ** 0.5


# ============================================     MAIN     ===========================================================


# Декоратор для замера времени выполнения функции
def release_time(foo):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        foo(*args, **kwargs)
        print((datetime.datetime.now() - start).total_seconds())
        return foo
    return wrapper


# Функция умнежения вектора на число с использованием List Comprehension
@release_time
def comprehension_multiply(vector):
    return [el*2 for el in vector]


# Функция умнежения вектора на число с использованием numpy (векторное умножение)
@release_time
def vector_multiply(vector):
    return np.array(vector)*2


# Функция выборки (фильтрации) с использованием List Comprehension
@release_time
def comprehension_filter(vector):
    return [el for el in vector if el % 2 == 0]


# Функция выборки (фильтрации) с использованием numpy
@release_time
def vector_filter(vector):
    return vector[vector % 2 == 0]


def main():

    # input_str = '1, 2, 3, 4, 5.0, 6, 7, 8, 9, 10'.split(',')
    # v1 = np.array(input_str, dtype=float)
    # print(v1)
    # comprehension_multiply(range(1, int(10e6)))
    # vector_multiply((range(1, int(10e6))))
    # comprehension_filter(range(1, int(10e6)))
    # vector_filter(np.array((range(1, int(10e6)))))

    # task1('1, 2, 3, 4', '10, 20, 30, 40')
    # print(task2('1, 2, 3, 4, 5, 6', '1, 2, 3, 4'))
    # print(task3(np.array('-1, 1'.split(','), dtype=float),
    #             np.array('2, 5'.split(','), dtype=float),
    #             np.array('5,-3'.split(','), dtype=float)))




if __name__ == '__main__':
    main()
