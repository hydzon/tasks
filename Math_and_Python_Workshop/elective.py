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

Напишите функцию wisdom_multiplication(x, y, length_check = True),
реализующую умножение по схеме мудреца с прошлого шага.
-Вычитаем из 100 первое и второе число.
-Складываем результаты шага 1.
-Вычитаем из 100 результат шага 2.
-Перемножаем результаты шага 1.
-Результат шага 3 даёт первые цифры результата, а результат шага 4 даёт последние 2 цифры результата.
В зависимости от значения аргумента length_check функция проверяет или нет длину результата шага 4 и
при необходимости дописывает 0 перед ним (если результат всего 1 цифра).
Функция должна возвращать целое число.

Напишите 2 функцию multiplication_check_list(start=10, stop=99, length_check = True)
Для проверки всех пар в интервале.
В зависимости от значения аргумента length_check добавляйте при необходимости 0 при конкатенации.
multiplication_check_list должна уметь печатать:
-Правильных результатов: n
-Неправильных результатов: m


7)Реализуйте функцию caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), возвращающую зашифрованный текст, работающую только с латинским алфавитом.
text - исходных текст, который надо зашифровать (или расшифровать)
key - ключ (сдвиг)
Ключ может быть отрицательным или больше 26
Из преобразуемого текста удаляются все пробелы и знаки препинания.
Зашифрованный текст пишется в верхнем регистре 1 строкой.
Ваша функция должна корректно работать с любым переданным алфавитом,
а если алфавит не передан, то использовать английский.

Реализуйте функцию bruteforce(text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), которая выводит на печать
все возможные "расшифровки" исходного текста.
Если алфавит не передан на вход функции, то считается, что текст на английском
(считаем, что определение алфавита производит оператор-человек).
Порядок вывода расшифровок от сдвига "-1" по убыванию (-1, -2, -3...)


Реализуйте функцию jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False),
возвращающую зашифрованный текст
text - исходный текст
key - ключ шифрования (число)
alphabet - алфавит (по умолчанию английский)
reverse - признак расшифровки, если находится в значении True, это значит, что функцию надо использовать
для расшифровки текста, т.к. каждый сдвиг должен быть отрицательным. (по умолчанию False)
Из преобразуемого текста удаляются все пробелы и знаки препинания.
Зашифрованный текст пишется в верхнем регистре 1 строкой.

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


# ============================================    tasks 5-6   ==========================================================


def simple_multiplication(x, y) -> int:
    return (100 - ((100 - x) + (100 - y))) * 100 + (100 - x) * (100 - y)


def wisdom_multiplication(x, y, length_check=True):
    n1 = str(100 - ((100 - x) + (100 - y)))
    n2 = str((100 - x) * (100 - y))
    if length_check and len(n2) == 1:
        n2 = '0' + n2
    return int(n1 + n2)


def multiplication_check(x, y, length_check=True):
    return x * y == wisdom_multiplication(x, y, length_check)


def multiplication_check_list(start=10, stop=99, length_check=True):
    result = [multiplication_check(x, y, length_check) for x in range(start, stop + 1) for y in range(start, stop + 1)]
    print(f'Правильных результатов: {result.count(True)}')
    print(f'Неправильных результатов: {result.count(False)}')


# ============================================    tasks 7   ==========================================================

def caesar(text: str, key: int, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    # alph = alphabet[(key % len(alphabet)):] + alphabet[:(key % len(alphabet))]
    encrypt_text = ''.join([alphabet[(alphabet.index(ch) + key) % len(alphabet)] for ch in text.upper() if ch in alphabet])
    # decrypt_text = ''.join([alphabet[alph.index(ch)] for ch in encrypt_text])
    # print(f'Encrypted:\n{encrypt_text}\nDecrypted back:\n{decrypt_text}')
    print(f'Encrypted:\n{encrypt_text}')
    bruteforce(encrypt_text, alphabet)


def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    print('Bruteforce:')
    for i in range(1, len(alphabet)):
        print(''.join([alphabet[(alphabet.index(ch) - i) % len(alphabet)] for ch in text]))


def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
        encrypt_text, decrypt_text = '', ''
        key = str(key)
        key_ind = 0
        for char in text.upper():
            if key_ind > len(key) - 1:
                key_ind = 0
            if char in alphabet:
                if reverse:
                    decrypt_text += alphabet[(alphabet.index(char) - int(key[key_ind])) % len(alphabet)]
                else:
                    encrypt_text += alphabet[(alphabet.index(char) + int(key[key_ind])) % len(alphabet)]
                key_ind += 1
        return decrypt_text
        # print(f'Decrypted:\n{decrypt_text}' if reverse else f'Encrypted:\n{encrypt_text}')


def bruteforce_jarriquez(text, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
    for i in range(1000, 1000000):
        dec_string = jarriquez_encryption(text, i, alphabet, reverse=True)
        if dec_string.count('алмаз'.upper()) or dec_string.count('Дакоста'.upper()):
            print(f'Ключ: {i}, Фраза: {dec_string}')
    print('Перебор завершен.')


# ============================================     MAIN     ============================================================


def main():
    plus_infinity = 10000000000

    # kaprekar_loop(103303)
    # print(fi(0, 1, 11))
    # print(super_L(5**4 * 3**4 * 2**4))
    # print(kaprekar(218400870420))
    # print(simple_multiplication(99, 91))
    # multiplication_check_list()
    # caesar('BQQMFZ', 0)
    # jarriquez_encryption('Вы судья Жаррикез из романа Жюля Верна "Жангада".', 1020, 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    # crypted_text = 'ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИ
    # ЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗК
    # ЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕК
    # ИБШМЦХЙИАМФЛУЬЙИСЗРТЕС'
    # bruteforce_jarriquez(crypted_text)

if __name__ == '__main__':
    main()
