"""
1) Напишите функцию на примере постоянной Капрекара.
Для любого 3, 4 или 6-значного числа n, в котором не все цифры одинаковы.

2) Напишите функцию luka(L0, L1, n), которая принимает на вход параметры:
L0, L1 - 0й и 1й члены последовательности соответственно
n - номер числа из последовательности, которое необходимо вернуть


3) Напишите функцию fi(L0, L1, n) такую что:
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


6) Напишите функцию simple_multiplication(x, y), реализующую умножение по схеме мудреца с прошлого шага:
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


7) Реализуйте функцию caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), возвращающую зашифрованный текст, работающую только с латинским алфавитом.
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


Напишите функцию disc_generator(alphabet), которая принимает на вход упорядоченный список (строку),
а возвращает случайным образом перемешанный (тоже строку).

Создайте функцию jefferson_encryption(text, discs, step, reverse=False), реализующую "цилиндр Джеферсона"
text - исходный текст
discs - список из словарей (строк)
step - сдвиг на которых смещаются символы с помощью алгоритма Цезаря (ключ шифрования для шифра Цезаря)
reverse - признак расшифровки, если находится в значении True, это значит, что функцию надо использовать
          для расшифровки текста, т.к. каждый сдвиг должен быть отрицательным. (по умолчанию False)


Реализуйте функцию шифрования, которую использовал пират Кидд из рассказа Эдгара Аллана По "Золотой жук".
Используйте словарь:
cypher = {'e': '8', 't': ';', 'h': '4', 'o': '‡', 's': ')', 'n': '*', 'a': '5', 'i': '6', 'r': '(', 'f': '1',
'd': '†', 'l': '0', 'm': '9', 'b': '2', 'y': ':', 'g': '3', 'u': '?', 'v': '¶', 'c': '-', 'p': '.'}


8)     ==== Э Н И Г М А  ====

Реализуйте функцию rotor(symbol, n, reverse=False)
symbol - символ, поступающий для шифрования
n - номер ротора
reverse - признак обратного направления, если находится в значении True, это значит, что функцию надо использовать
в обратном направлении. (по умолчанию False)
Возвращает строку с зашифрованным символом


Реализуйте функцию reflector(symbol, n):
symbol - символ, поступающий для шифрования
n - номер отражателя


Реализуйте функцию enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3) с поворачивающимися роторами,
как они описаны на предыдущем шаге.
text - исходный текст, который необходимо зашифровать
ref - номер отражателя (согласно задаче https://stepik.org/lesson/283487/step/3)
rot1, rot2, rot3 - номера роторов (согласно задаче https://stepik.org/lesson/283487/step/2)
shift1, shift2, shift3 - сдвиги роторов (1, 2 и 3, соответственно)


"""
import random
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
    # encrypt_text = ''.join([alphabet[(alphabet.index(ch) + key) % len(alphabet)]
    # for ch in text.upper() if ch in alphabet])
    # decrypt_text = ''.join([alphabet[alph.index(ch)] for ch in encrypt_text])
    # print(f'Encrypted:\n{encrypt_text}\nDecrypted back:\n{decrypt_text}')
    # print(f'Encrypted:\n{encrypt_text}')
    # bruteforce(encrypt_text, alphabet)
    return ''.join([alphabet[(alphabet.index(ch) + key) % len(alphabet)] for ch in text.upper() if ch in alphabet])

def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    print('Bruteforce:')
    for i in range(1, len(alphabet)):
        print(''.join([alphabet[(alphabet.index(ch) - i) % len(alphabet)] for ch in text]))


def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
        encrypt_text, decrypt_text = '', ''
        key = str(key)
        key_index = 0
        for char in text.upper():
            if key_index > len(key) - 1:
                key_index = 0
            if char in alphabet:
                if reverse:
                    decrypt_text += alphabet[(alphabet.index(char) - int(key[key_index])) % len(alphabet)]
                else:
                    encrypt_text += alphabet[(alphabet.index(char) + int(key[key_index])) % len(alphabet)]
                key_index += 1
        return decrypt_text
        # print(f'Decrypted:\n{decrypt_text}' if reverse else f'Encrypted:\n{encrypt_text}')


def bruteforce_jarriquez(text, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
    for i in range(1000, 1000000):
        dec_string = jarriquez_encryption(text, i, alphabet, reverse=True)
        if dec_string.count('алмаз'.upper()) or dec_string.count('Дакоста'.upper()):
            print(f'Ключ: {i}, Фраза: {dec_string}')
    print('Перебор завершен.')


def disc_generator(alphabet):
    rand_alph = list(alphabet)
    random.shuffle(rand_alph)
    return ''.join(rand_alph)


def jefferson_encryption(text, discs, step, reverse=False):
    encrypt_text, decrypt_text = '', ''
    discs_index = 0
    for char in text.upper():
        if discs_index > len(discs) - 1:
            discs_index = 0
        if char in discs[discs_index]:
            if reverse:
                decrypt_text += caesar(char, -step, discs[discs_index])
            else:
                encrypt_text += caesar(char, step, discs[discs_index])
            discs_index += 1
    print(f'Decrypted:\n{decrypt_text}' if reverse else f'Encrypted:\n{encrypt_text}')


l1 = ['e', 't', 'h', 'o', 's', 'n', 'a', 'i', 'r', 'f', 'd', 'l', 'm', 'b', 'y', 'g', 'u', 'v', 'c', 'p']
l2 = ['8', ';', '4', '‡', ')', '*', '5', '6', '(', '1', '†', '0', '9', '2', ':', '3', '?', '¶', '-', '.']
def kidds_encryption(text, reverse=False):
    if reverse:
        return ''.join([l1[l2.index(ch)] for ch in text.lower()])
    else:
        return ''.join([l2[l1.index(ch)] for ch in text.lower() if ch in l1])


# ============================================    Э Н И Г М А   ========================================================

ROTORS = {
    0: ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
    2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
    3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N'),
    4: ('AEPLIYWCOXMRFZBSTGJQNH', 'DV', 'KU'),
    5: ('AVOLDRWFIUQ', 'BZKSMNHYC', 'EGTJPX'),
    6: ('AJQDVLEOZWIYTS', 'CGMNHFUX', 'BPRK'),
    7: ('ANOUPFRIMBZTLWKSVEGCJYDHXQ'),
    8: ('AFLSETWUNDHOZVICQ', 'BKJ', 'GXY', 'MPR'),
    'beta': ('ALBEVFCYODJWUGNMQTZSKPR', 'HIX'),
    'gamma': ('AFNIRLBSQWVXGUZDKMTPCOYJHE')
}
REFLECTORS = {
    0: (),
    1: ('AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW'),
    2: ('AF', 'BV', 'CP', 'DJ', 'EI', 'GO', 'HY', 'KR', 'LZ', 'MX', 'NW', 'TQ', 'SU'),
    3: ('AE', 'BN', 'CK', 'DQ', 'FU', 'GY', 'HW', 'IJ', 'LO', 'MP', 'RX', 'SZ', 'TV'),
    4: ('AR', 'BD', 'CO', 'EJ', 'FN', 'GT', 'HK', 'IV', 'LM', 'PW', 'QZ', 'SX', 'UY')
}


def rotor(symbol, rotor_name, reverse=False):
    symbol = symbol.upper()
    if rotor_name:
        for rotor_word in range(len(ROTORS[rotor_name])):
            if symbol in ROTORS[rotor_name][rotor_word]:
                search_word = ROTORS[rotor_name][rotor_word]
                symbol = search_word[(search_word.index(symbol) - 1) % len(search_word)] if reverse \
                    else search_word[(search_word.index(symbol) + 1) % len(search_word)]
                break
    return symbol


def reflector(symbol, n):
    symbol = symbol.upper()
    for ref_word in range(len(REFLECTORS[n])):
        if symbol in REFLECTORS[n][ref_word]:
            search_word = REFLECTORS[n][ref_word]
            symbol = search_word[(search_word.index(symbol) - 1) % len(search_word)]
            break
    return symbol


def encrypted(symbol, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    symbol = ROTORS[0][(ROTORS[0].index(symbol) + shift3) % len(ROTORS[0])]
    symbol = rotor(symbol, rot3)
    symbol = ROTORS[0][(ROTORS[0].index(symbol) + (shift2 - shift3)) % len(ROTORS[0])]
    symbol = rotor(symbol, rot2)
    symbol = ROTORS[0][(ROTORS[0].index(symbol) + (shift1 - shift2)) % len(ROTORS[0])]
    symbol = rotor(symbol, rot1)
    symbol = ROTORS[0][(ROTORS[0].index(symbol) - shift1) % len(ROTORS[0])]
    symbol = reflector(symbol, ref)
    symbol = ROTORS[0][(ROTORS[0].index(symbol) + shift1) % len(ROTORS[0])]
    symbol = rotor(symbol, rot1, reverse=True)
    symbol = ROTORS[0][(ROTORS[0].index(symbol) - (shift1 - shift2)) % len(ROTORS[0])]
    symbol = rotor(symbol, rot2, reverse=True)
    symbol = ROTORS[0][(ROTORS[0].index(symbol) - (shift2 - shift3)) % len(ROTORS[0])]
    symbol = rotor(symbol, rot3, reverse=True)
    symbol = ROTORS[0][(ROTORS[0].index(symbol) - shift3) % len(ROTORS[0])]
    return symbol


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    encrypted_text = ''
    for ch in text.upper():
        if ch in ROTORS[0]:
            encrypted_text += encrypted(ch, ref, rot1, shift1, rot2, shift2, rot3, shift3)
    return encrypted_text


# ============================================     MAIN     ============================================================


def main():
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

    # print(disc_generator('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # discs = [disc_generator('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6)]
    # discs = ['QMJZTGFKPWLSBOXNCRYEVHIADU', 'CVMHTPQXZJLWORBDUGEYKNFAIS', 'AMPKIXVFQEWODNZYHBCGSLTUJR',
    #          'NMPJZSBAQDILKEGOYHRFXTCUVW', 'JHANFBRXVQYTLDCIEOMPUZKWSG', 'ZHJLSWGXQBKAPYIORMCTNVFUED']
    # jefferson_encryption('Some encripted text', discs, 13, reverse=False)
    # print(kidds_encryption('ethosnairfdlmbyguvcp'))

    # print(rotor('b', 0, reverse=True))
    # print(reflector('b', 1))
    print(enigma('Some encripted text', 1, 1, 1, 2, 2, 3, 1))



if __name__ == '__main__':
    main()
