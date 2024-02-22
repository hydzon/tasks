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


4) Переменная M1 содержит Numpy матрицу.
Произведите операции последовательно:
- Замените значения в предпоследней строке на значения по формуле
- Замените значения в предпоследнем столбце на значения по формуле: e^x
Результат запишите в переменную M2


5) Считайте строку, где значения заданы через пробел shape и dtype
Последнее значение в строке может быть либо числом (тогда это последнее значение кортежа shape), либо строкой dtype
shape - атрибут, задающий размеры матрицы нолей (позволяет вернуть вектор-строку, вектор-столбец, матрицу, куб и т.д.)
dtype - тип данных, использующихся для значений матрицы. По-умолчанию используется numpy.float64.
Создайте матрицу Z размера shape, со значениями типа dtype (если dtype не указан, используйте numpy.float64)

Посчитайте размер матрицы Z в байтах и выведите его на печать.


6) Считайте 2 числа:
n - размер Numpy вектора
x - координата элемента вектора, который должен быть равен 1. Остальные элементы вектора должны быть равны 0.

Считайте 2 числа n, m.
Создайте вектор Z состоящий из чисел от n до m с шагом 1.

Дан вектор Z
"Разверните" его.


7) Считайте 3 числа:
n - количество элементов матрицы
m и k - размеры матрицы (число строк и столбцов соответственно)
Заполните матрицу Z числами от 0 до n-1 по порядку (сперва строки, потом столбцы).
Гарантируется, что m*k = n, т.е. все элементы "влезут" в матрицу и не останется пустых мест.


8) Дана матрица чисел Z (Z может быть 1, 2 или даже 3 мерной).
Выведите на печать список чисел из этой матрицы, которые больше 3.


9) Считайте 3 числа: n, m, l.
Создайте матрицу n*m*l из случайных чисел (от 0 до 1).


10) Создайте матрицу n*m из случайных чисел (от 0 до 1).
Выведите на печать значение минимального и максимального чисел в получившейся матрице (каждое с новой строки).

Выведите на печать значение среднего для всей матрицы.


11) Создайте матрицу n*m из случайных чисел (от 0 до 1).
Найдите среднее значение для каждого из столбцов.
Выведите на печать значение минимального и максимального среднего по столбцам.


12) Создайте матрицу размера n*m такую что:
На границе матрицы будут стоять 1
Внутри матрицы будут стоять 0

"""

import datetime
from functools import reduce

import numpy as np

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


def task4(input_array):
    input_array[input_array.shape[0] - 2] = np.sin(input_array[input_array.shape[0] - 2] * np.pi / 6)
    input_array[:, input_array.shape[0] - 2] = np.exp(input_array[:, input_array.shape[0] - 2])
    print(np.round(input_array, 2))


def task5(input_str):
    input_str = [int(el) if el.isdigit() else el for el in input_str.split(' ')]
    z = np.zeros((input_str[:-1]), input_str[-1]) if type(input_str[-1]) is str else np.zeros(input_str, np.float64)
    # s = reduce(lambda x, y: x * y, z.shape)
    s = z.size * z.itemsize
    return z, s


# ============================================     tasks 6-10   =========================================================


def task6(n, x):
    return np.array([1 if el == x else 0 for el in range(n)], np.float64)


def task6_1(n, m, s=1):
    return np.arange(n, m, s)


def task6_2(vector):
    return vector[::-1]


def task7(n, m, k):
    return np.arange(n).reshape(m, k)


def task8(z):
    return list(z[(z > 3)])  # Накладываем на исходную матрицу, матрицу с условием, и получем только подходящие элементы


def task9(n, m, l):
    return np.random.random_sample((n, m, l))


def task10(n, m):
    z = np.sort(np.random.random_sample((n, m)), axis=0)
    av = np.average(z)
    return z[0, 0], z[1, 1], av


# ============================================     tasks 11-15   =======================================================


def task11(n, m):
    z = np.random.random_sample((n, m))
    av = np.mean(z, axis=0)
    print(np.amin(av), np.amax(av), sep='\n')


def task12(n, m):
    z = np.zeros((n, m))
    z[:, 0] = z[:, -1] = z[0] = z[-1] = 1
    print(z)

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

    # m1 = np.array((
    #     (1., 2., 3., 0.),
    #     (4., 5., 6., 0.),
    #     (0., 1., 1., 6.),
    #     (7., 8., 9., 0.)
    # ))
    # task4(m1)

    # print(np. zeros(5, bool))
    # print(task5('3'))
    # np.info(np.add)
    # ar = np.array(0)
    # np.info(ar)

    # print(task6_2(np.array([1, 2, 3, 4])))
    # print(task7(9, 3, 3))
    # np.array(3).nonzero()

    # print(task8(np.array([1, 2, 3, 4])))
    # print(task10(10, 10))
    # task11(5, 7)
    # task12(5, 5)

    print(3 * 0.1)

if __name__ == '__main__':
    main()
