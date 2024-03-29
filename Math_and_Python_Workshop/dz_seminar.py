"""
1) Реализуйте функцию f(x)=2arctg(x)
Найдите предел функции (ответ округлите до 3 знака после запятой) при x→+∞


2) Проверьте (для нескольких разных точек), что производная от e^x совпадает с исходной функцией.
Для этого реализуйте функцию def_e(x), находящую численное значение производной (с точностью до 3 знака) в точке x.


3) Напишите функцию even_indexes(L), которая будет возвращать только элементы с чётными индексами.

4) Напишите функцию even_elements(l), которая возвращает только чётные элементы списка.

5) Считайте строку (используйте input()), содержащую 1 натуральное число n
Найдите сумму всех чисел от 0 до n, включительно, которые делятся на 5 без остатка, но на 3 делятся с остатком.

6) Напишите функцию common(list_a, list_b), возвращающую список общих элементов 2 списков (порядок не важен).

7) Напишите функцию front_x(words), которая на вход принимает список строк и возвращает отсортированный по правилам:
    -слова, начинающиеся с символа "x", идут первыми
    -в лексикографическом порядке.
Список может содержать пустые строки - "" - их нельзя выкидывать и при их обработке функция не должна "падать".

"""


# ============================================     tasks  ===========================================================
from math import *


def task1(x):
    return round(2 * atan(x), 3)


def def_e(x):
    dx = 0.0000001
    return round((exp(x + dx) - exp(x)) / dx, 3)


def even_indexes(L):
    return L[::2]


def even_elements(li):
    return [el for el in li if el % 2 == 0]


def task5(n):
    return sum([x for x in range(n + 1) if x % 5 == 0 and x % 3 != 0])


def common(list_a, list_b):
    # return [x for x in list_a if x in list_b]
    return list(set(list_a) & set(list_b))


def front_x(words):
    tmp_list = sorted([el for el in words if el and el[0] == 'x'])
    tmp_list += sorted([el for el in words if (el and el[0] != 'x') or len(el) == 0])
    return tmp_list


def donuts(count):
    return 'Всего пончиков: ' + (str(count) if count < 10 else 'много')


def both_ends(s):
    return s[:2] + s[-2:] if len(s) > 1 else ''


def fix_start(s):
    # return s[0] + ''.join([lit if lit != s[0] else '*' for lit in s[1:]])
    return s[0] + s[1:].replace(s[0], '*')    # лучше так

# ============================================     MAIN     ===========================================================


plus_infinity = 10000000000


def main():
    lim = task1(plus_infinity)
    print(lim)

    x = 0.2
    print(exp(x))
    print(def_e(x))

    print(even_indexes([1, 1, 2, 3, 5, 8, 13, 21, 34]))
    print(even_elements([1, 1, 2, 3, 5, 8, 13, 21, 34]))

    print(task5(100))

    print(common([0, 2, 3, 4, 5, 19, 42], [0, 6, 19, 33, 42, 55, 66, 77, 99, 101, 256]))

    print(front_x(['mix', 'extra', 'x-files', '', 'xyz', 'xapple', 'apple']))

    print(donuts(8))
    print(both_ends('ygugh'))
    print(fix_start('babble'))


if __name__ == '__main__':
    main()
