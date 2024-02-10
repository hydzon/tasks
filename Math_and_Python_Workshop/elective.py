"""
1) функции на примере постоянной Капрекара.
Для любого четырёхзначного числа n, больше 1000, в котором не все цифры одинаковы.


2)Напишите функцию numerics(n), принимающую на вход 1 натуральное 4х значное число,
а возвращающую список цифр из которых состоит число.
Если какая-то цифра встречается в исходном числе несколько раз, то и в ответе она должна встретиться несколько раз.
Порядок цифр в ответе не важен.

"""


# ============================================     tasks  ===========================================================
from math import *


def permanent_caprecar(n):
    for i in range(7):
        n_sorted = int(''.join(sorted(str(n))))
        n_sorted_rev = int(''.join(sorted(str(n), reverse=True)))
        if n_sorted > n_sorted_rev:
            n = n_sorted - n_sorted_rev
        else:
            n = n_sorted_rev - n_sorted
        if n == 6174:
            break
    return n


def numerics(n):
    # return [int(num) for num in str(n)]
    return list(map(int, str(n)))



# ============================================     MAIN     ===========================================================


def main():
    plus_infinity = 10000000000

    print(permanent_caprecar(9909))
    print(numerics(9909))

if __name__ == '__main__':
    main()
