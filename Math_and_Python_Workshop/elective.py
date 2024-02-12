"""
1) функции на примере постоянной Капрекара.
Для любого четырёхзначного числа n, больше 1000, в котором не все цифры одинаковы.


2)Напишите функцию numerics(n), принимающую на вход 1 натуральное 4х значное число,
а возвращающую список цифр из которых состоит число.
Если какая-то цифра встречается в исходном числе несколько раз, то и в ответе она должна встретиться несколько раз.
Порядок цифр в ответе не важен.

"""
from functools import reduce
# ============================================     tasks  ===========================================================
from math import *


def permanent_caprecar(n):
    for i in range(7):
        n_sorted = int(''.join(sorted(str(n))))
        n_sorted_rev = int(''.join(sorted(str(n), reverse=True)))
        n = n_sorted_rev - n_sorted
        if n == 6174:
            break
    return n


def numerics(n):
    # return [int(num) for num in str(n)]
    return list(map(int, str(n)))


def kaprekar_step(L):
    sort_L = int(''.join(list(map(str, sorted(L)))))
    rev_L = int(''.join(list(map(str, sorted(L, reverse=True)))))
    return rev_L - sort_L


def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
    else:
        print(n)
        list_n = {n}
        while n not in (495, 6174, 549945, 631764):
            n = kaprekar_step(numerics(n))
            if n in list_n:
                print(f'Следующее число - {n}, кажется процесс зациклился...')
                break
            else:
                print(n)
                list_n.add(n)


def kaprekar_check(n):
    if len(numerics(n)) in [3, 4, 6]:
        if len(set(numerics(n))) != 1:
            if n not in [100, 1000, 100000]:
                return True
    return False
# ============================================     MAIN     ===========================================================


def main():
    plus_infinity = 10000000000

    kaprekar_loop(103303)


if __name__ == '__main__':
    main()
