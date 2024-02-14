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


4)Напишите функцию kaprekar(n), принимающую на вход натуральное число и возвращающую:
True, если число является Числом Капрекара
False, если число НЕ является Числом Капрекара


5) Напишите функцию convert(num, to_base=10, from_base=10), переводящую число из одной системы счисления в другую,
которая принимает на вход:
- целое число num (может быть int в десятичной системе счисления, либо строкой в произвольной)
- 2 целочисленных необязательных аргумента to_base и from_base со значениями по умолчанию 10,
основанием исходной и будущей систем отстчёта.


6)Напишите функцию simple_multiplication(x, y), реализующую умножение по схеме мудреца с прошлого шага:
x*y = (100−((100−x)+(100−y)))⋅100+(100−x)⋅(100−y)

Напишите функцию multiplication_check(x, y), которая будет проверять корректность работы методом мудреца
для умножения чисел x и y. Результат работы функции - логическое значение (True/False).

Напишите функцию multiplication_check_list(start=10, stop=99), которая по умолчанию будет проверять весь интервал двузначных чисел
(если никакие параметры не переданы), но так же позволит проверять и произвольные интервалы
(например, от 15 до 20)
Функция должна уметь печатать 2 строки:
-Правильных результатов: n
-Неправильных результатов: m
Примечание. Пары, где числа поменялись местами считаются РАЗНЫМИ.



"""


# ============================================   tasks 1-5  ============================================================

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


def L2n(n):
    return super_L(n) ** 2 - 2 * (-1) ** n
def L3n(n):
    Ln = super_L(n)
    return Ln ** 3 - 3 * (-1) ** n * Ln
def L4n(n):
    Ln = super_L(n)
    return Ln ** 4 - 4 * (-1) ** n * Ln ** 2 + 2
def L5n(n):
    Ln = super_L(n)
    return Ln ** 5 - 5 * (-1) ** n * Ln ** 3 + 5 * Ln


def super_L(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return L2n(n//2)
    elif n % 3 == 0:
        return L3n(n//3)
    elif n % 4 == 0:
        return L3n(n//4)
    elif n % 5 == 0:
        return L5n(n//5)
    else:
        return super_L(n - 1) + super_L(n - 2)


def kaprekar(n):
    sq = str(n ** 2)
    for i in range(1, len(sq)):
        if int(sq[i:]) > 0 and int(sq[:i]) + int(sq[i:]) == n:
            return True
    return False


nums_in_si36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert_to(num, from_base, to_base):
    if from_base == 10:
        num = int(num)
        if num // to_base == 0:
            return nums_in_si36[num % to_base]
        return convert_to(num // to_base, from_base, to_base) + nums_in_si36[num % to_base]
    else:
        to_10 = 0
        num = str(num)
        for i in range(len(num)):
            to_10 += nums_in_si36.index(num[-(i + 1)]) * from_base ** i
        return convert_to(to_10, 10, to_base)


def convert(n, from_base=10) -> str:
    si = (2, 8, 10, 16, 35)
    for i in si:
        if from_base != i:
            print('{} в системе с основанием {} => {} в системе с основанием {}'
                  .format(n, from_base, convert_to(n, from_base, i), i))


# ============================================    tasks 5-... ==========================================================


def simple_multiplication(x, y) -> int:
    return (100 - ((100 - x) + (100 - y))) * 100 + (100 - x) * (100 - y)


def multiplication_check(x, y):
    return x * y == simple_multiplication(x, y)


def multiplication_check_list(start=10, stop=99):
    result = [multiplication_check(x, y) for x in range(start, stop + 1) for y in range(start, stop + 1)]
    print(f'Правильных результатов: {result.count(True)}')
    print(f'Неправильных результатов: {result.count(False)}')


# ============================================     MAIN     ============================================================


def main():
    plus_infinity = 10000000000

    # kaprekar_loop(103303)
    # print(fi(0, 1, 11))
    # print(super_L(5**4 * 3**4 * 2**4))
    # print(kaprekar(218400870420))
    # print(multiplication_check(96, 97))
    multiplication_check_list()


if __name__ == '__main__':
    main()
