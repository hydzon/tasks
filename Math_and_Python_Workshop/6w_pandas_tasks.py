"""
1)

"""

import numpy as np
import pandas as pd


# ============================================     tasks 1-5   =========================================================


def task1(z):
    pass


# ============================================     MAIN     ===========================================================


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

critical_age = 3


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


if __name__ == '__main__':
    main()
