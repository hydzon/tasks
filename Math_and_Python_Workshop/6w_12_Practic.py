"""
The cat's task

Практикум для решения задачи нахождения сходства текстов

"""

import numpy as np
import pandas as pd
import re
from scipy.spatial.distance import cosine


def formating_text(a, b):
    list_words = []
    list_strings = []
    with open('text.txt', 'r') as file:
        for string in file.readlines():
            tmp_string = [el for el in re.split('[^a-z0-9]', string.lower()) if el]
            list_strings.append(tmp_string)
            list_words.extend(tmp_string)

    i = 0
    dict_words = dict()
    for word in list_words:
        if word not in dict_words:
            dict_words[word] = i
            i += 1

    objects_and_attributes = np.zeros((len(list_strings), len(dict_words)))
    for i in range(len(list_strings)):
        for j in range(len(list_strings[i])):
            objects_and_attributes[i, dict_words[list_strings[i][j]]] += 1

    return cosine(objects_and_attributes[a], objects_and_attributes[b])


# ============================================     MAIN     ===========================================================


def main():
    # # Шаг 1: Пересчитать число строк с текстом в файле.
    # with open('text.txt', 'r') as file:
    #     strings_with_text = [string for string in file.readlines() if len(string) > 2]
    #     print(len(strings_with_text))
    #
    # # Шаг 2: Напечатайте в 1 строку все 1-е символы из каждого слова через пробел.
    # for el in strings_with_text:
    #     print(' '.join(word[0] for word in el.split()))
    #
    # # Шаг 2.2: Выведите на печать в одну строку начальные символы из каждой строки файла.
    # # В качестве разделителя используйте пробел.
    # with open('dataset_48784_9.txt', 'r') as file:
    #     print(' '.join(string[0] for string in file.readlines()))
    #
    # # Шаг 3: Приводим к нижнему регистру, разрезаем предложение, удаляем пустые строки
    # list_1 = re.split('[^a-z]', strings_with_text[0])
    # print([el for el in list_1 if el])
    #
    # # Шаг 4: Вытянуть двумерный список в одномерный
    # strings_with_text = [el.split() for el in strings_with_text]
    # # tmp = []
    # # [tmp.extend(el) for el in strings_with_text]
    # print(sum(strings_with_text, []))

    print(formating_text(0, 4))


if __name__ == '__main__':
    main()
