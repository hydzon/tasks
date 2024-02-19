"""
1) Найдите предел функции f(x)
x→+∞
x→−∞
Ответ округлите до 3 знака после запятой.


2) Напишите функцию derivative(f, x0=0), находящую производную функции
f(x) в точке x=x0
Функция должна принимать 2 параметра:
обязательный - f - имя функции (без скобочек)
необязательный - x0 - значение аргумента точки в которой вычисляется производная.
Если не задан, то значение будет равно 0.
Функция должна округлять ответ до 3 знака после запятой.


3) Напишите функцию list_pull(L), принимающую на вход многомерный список (список списков)
и возвращающую "вытянутый" список только значений


4)Не используя метод deepcopy скопируйте всё содержимое списка L1 в L2.


5)Напишите функцию verbing(s), принимающую на вход строку.
Если длина строки 3 и больше, то добавьте к ней 'ing' в конце
Если строка уже содержит 'ing', добавьте 'ly'
Если длина строки меньше 3, верните строку как есть


6)Напишите функцию front_back(a, b), принимающую 2 строки, a и b, и возвращающую строку формы
a-front + b-front + a-back + b-back


7) Напишите функцию mimic_dict(string), которая принимает на вход строковую переменную (может содержать пробелы,
табуляцию, переносы строк), возвращающую «имитирующий» словарь, который соотносит каждое появившееся слово,
со списком всех слов, которые следуют за этим словом.
Для "входа" в словарь используйте в качестве ключа пустую строку, в соответствие которой будет поставлено 1 слово.


8) Напишите функцию print_mimic(mimic_dict, word), которая принимает на вход 2 параметра:
словарь, идентичный тому который возвращает mimic_dict(string) из предыдущей задачи
строку (1-е слово, с которого надо начать текст)


"""

# ============================================     tasks 1-5   ===========================================================

from math import *
import re
import random


def f(x):
    return (2 * x**2 - 3 * x - 5) / (3 * x**2 + x + 1)


def f2(x):
    return sin(pi * x / 2) / x


def derivative(fun, x0=0):
    dx = 0.00001
    return (fun(x0+dx) - fun(x0)) / dx


def list_pull(input_list):
    s = []
    for el in input_list:
        if type(el) is list:
            s.extend(list_pull(el))
        else:
            s.append(el)
    return s


def my_deepcopy(input_list):
    return [my_deepcopy(el) if isinstance(el, list) else el for el in input_list]


def verbing(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'


# ============================================     tasks 6-...  ========================================================


def front_back(a, b):
    return a[:round(len(a)/1.9999)] + b[:round(len(b)/1.9999)] + a[round(len(a)/1.9999):] + b[round(len(b)/1.9999):]


def mimic_dict(string: str):
    list_words = re.split(' |\n|    ', string)
    list_words = [el for el in list_words if len(el) > 0]
    dict_words = {'': [list_words[0]]}
    for i in range(len(list_words) - 1):
        if list_words[i] not in dict_words:
            s = set()
            for j in range(len(list_words)):
                if list_words[j] == list_words[i] and j != len(list_words) - 1:
                    s.add(list_words[j + 1])
            dict_words[list_words[i]] = list(s)
    return dict_words


def print_mimic(mimic_dict, word):
    text = []
    while len(text) < 20:
        text.append(word)
        if word in mimic_dict:
            word = random.choice(mimic_dict[word])
        else:
            word = mimic_dict[''][0]
    return ' '.join(text)


# ============================================     MAIN     ===========================================================


def main():
    # print(round(f(1e10), 3))
    # print(round(f(-1e10), 3))
    # print(round(f2(1e10), 3))
    # print(round(f2(2), 3))

    # print(list_pull([['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]))

    # l1 = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]
    # l2 = my_deepcopy(l1)
    # l1[2][0] = 1
    # print(l1)
    # print(l2)

    # print(verbing('swiming'))

    # print(front_back('absdc', '11211'))
    # print(round(5/1.9))

    print(print_mimic(mimic_dict('a cat and a dog\na fly    '), ''))


if __name__ == '__main__':
    main()
