"""
1) В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит,
когда с момента исходной даты date пройдет число дней, равное days.

2) Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
Вам необходимо узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.
Ответом для данной задачи служит расшифрованная интересная информация Алисы.

3) Реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный класс filter,
но будет использовать не одну функцию, а несколько.

4) Реализуйте функцию-генератор primes, которая будет генерировать простые числа
в порядке возрастания, начиная с числа 2.

"""

import datetime
import itertools
import math

from simplecrypt import encrypt, decrypt
from collections import Counter

# ============================================     tasks 1-2   =========================================================


def task1():
    date = datetime.date(*map(int, input().split()))
    date += datetime.timedelta(int(input()))
    print(f'{date.year} {date.month} {date.day}')


def task2():
    with open("encrypted.bin", "rb") as inp:
        encrypted = inp.read()
        with open("passwords.txt", "r") as ps_file:
            passwords = [ps[:-1] for ps in ps_file.readlines()]
            print(passwords)
        for el in enumerate(passwords):
            try:
                print(decrypt(el[1], encrypted))
                break
            except Exception as e:
                print(f'Пароль {el[1]} не подошел')


# ============================================     task 3  =========================================================


class MultiFilter:
    def judge_half(pos, neg):
        return pos >= neg
        # допускает элемент, если его допускает хотя бы половина фукнций ()

    def judge_any(pos, neg):
        return pos >= 1
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0
        # допускает элемент, если его допускают все функции ()

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # исходная последовательность
        self.funcs = funcs  # допускающие функции
        self.judge = judge  # решающая функция
        print(self.funcs)

    def __iter__(self):
        for el in self.iterable:
            res = Counter([foo(el) for foo in self.funcs])
            if self.judge(res[True], res[False]):
                yield el


# ============================================     tasks   =========================================================

def primes():
    prime = 2
    while True:
        is_prime = True
        for i in range(2, prime):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            yield prime
        prime += 1


# ============================================     MAIN     ===========================================================
def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


def main():
    # task1()
    # task2()

    # a = [i for i in range(31)]
    # print(list(MultiFilter(a, mul2, mul3, mul5, judge=MultiFilter.judge_half)))

    print(list(itertools.takewhile(lambda x: x <= 100, primes())))


if __name__ == '__main__':
    main()

