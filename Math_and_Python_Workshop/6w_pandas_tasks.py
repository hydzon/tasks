"""
1) Выведите на печать сумму всех возрастов в df.

"""

import numpy as np
import pandas as pd


# ============================================     tasks 1-5   =========================================================

def task1(df):
    return df.age.sum()


# ============================================     MAIN     ===========================================================


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 2, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

critical_age = 3

filter_names = ["animal", "age"]
filter_values = ["cat", 3]
age_between = [2, 4]


def main():
    df = pd.DataFrame(data, index=labels)

    # print(df['animal']['e'])                 #Доступ к данным фрэйма
    # df.info()                                #DataFrame.info()
    # print(df.describe()['age']['75%'])       #DataFrame.describe
    # print(df[:3])                            #Срезы тоже работают
    # print(df.iloc[[0, 2, 3]])                # Доступ к строкам по индексам,еще можно использовать использовать loc()
    # print(df[['animal', 'age']])                      # Доступ к столбцам по имненам
    # print(df[['animal', 'age']].iloc[[0, 2, 3]])      # Вывод по названию столбцов и инндексам строк
    # print(df[df['age'] > critical_age])               # Применение фильтра
    # print(df[df['age'].isnull()])                     # Фильтр по незаполненым ячейкам

    # Примнение фильтров
    # print(df[(df[filter_names[0]] == filter_values[0]) & (df[filter_names[1]] <= filter_values[1])])

    # Дипазонный фильтр:
    # print(df[(df["age"] >= age_between[0]) & (df["age"] <= age_between[1])])
    # Либо так:
    # print(df[df['age'].between(*age_between)])

    # Увеличьте значение возраста в строке индексом равным index на 1.
    # df.loc['f', 'age'] += 1        # или так: df.age[index] += 1
    # print(df)
    # Увеличьте значение возраста во всех строках на 1
    # df.age += 1
    # print(df)

    # print(task1(df))            # Сумма по столбцу

    # Выведите на печать для каждого столбца, содержащего числа его имя и сумму через двоеточие.
    # for col in df.columns:
    #     if type(df[col].sum()) is np.float64 or type(df[col].sum()) is np.int64:
    #         print(f'{col}:{df[col].sum()}')
    # # а можно так:
    # for col in df.describe():
    #     print(f'{col}:{df[col].sum()}')

    # Найти средние значение возраста по всем записям, сгруппированным по значению в колонке
    # print(df.groupby('animal').age.mean())

    # Добавьте новую строку (с индексом new_index и значениями new_data) и удалите одну из старых (del_index)
    # new_index = "k"
    # new_data = [5.5, "dog", "Belka", "no"]
    # del_index = "f"
    # df = df.drop(del_index)
    # df.loc[new_index] = new_data
    # print(df)

    # Количество записей каждого типа, сгруппированным по значению в колонке
    # print(df['animal'].value_counts())

    # Cортирует сперва по уменьшению 1 поля из списка by, а при равенстве значений по увеличению 2.
    # print(df.sort_values(by=['animal', 'visits'], ascending=[False, True]))

    # Замена значений в столбце
    # df.priority = df.priority.map({'yes': True, 'no': False, 1: True, 0: False})
    # и еще одна замена
    # df['animal'] = df['animal'].replace('snake', 'python')


if __name__ == '__main__':
    main()
