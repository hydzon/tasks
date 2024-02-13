"""
1) функции на примере постоянной Капрекара.
Для любого 3, 4 или 6-значного числа n, в котором не все цифры одинаковы.

2)Напишите функцию luka(L0, L1, n), которая принимает на вход параметры:
L0, L1 - 0й и 1й члены последовательности соответственно
n - номер числа из последовательности, которое необходимо вернуть


3)Напишите функцию fi(L0, L1, n) такую что:
L0, L1 - 0й и 1й члены последовательности Люка соответственно
n - номер числа из последовательности, которое необходимо вернуть
Возвращаемое значение - это отношение 2 членов последовательности: Ln/Ln−1
В данной задаче нам очень важна точность вычислений. Поэтому мы будем использовать необычный тип данных - Decimal
"""

# ============================================     tasks  ===========================================================

from functools import reduce
from math import *
from decimal import *
getcontext().prec = 50


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


def luka(L0, L1, n):
    # return L0 + L1 if n <= 2 else luka(L1, L0 + L1, n - 1)   -  Рекурсивный вариант
    for _ in range(0, n):
        L0, L1 = L1, L0 + L1
    return L0


def fi(L0, L1, n):
    for _ in range(0, n - 1):
        L0, L1 = L1, L0 + L1
    return Decimal(L1)/Decimal(L0)
# ============================================     MAIN     ==== =======================================================


def main():
    plus_infinity = 10000000000

    # kaprekar_loop(103303)
    print(fi(0, 1, 11))


if __name__ == '__main__':
    main()
