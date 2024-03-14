"""
1) На столе лежат n кучек (n > 2) в каждой из которых какое-то кол-во бумажек.
Разрешается за 1 ход игры добавить к 2 любым кучкам по 1 бумажке.
Можно ли по правилам игры уравнять число бумажек в кучках?

Показать минимальное число ходов за которое можно уравнять число бумажек.




"""

import numpy as np
import requests
import os
import json

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================     tasks 1-5   =========================================================


def task1(inp):
    if (sum(inp) % 2 != 0) and (len(inp) % 2 == 0):
        print('Кучки нельзя уравнять')
    else:
        print('Кучки можно уравнять')
        if (max(inp) * len(inp) - sum(inp)) % 2 != 0:
            print(f'За {int(((max(inp) + 1) * len(inp) - sum(inp)) / 2)} ходов по {(max(inp) + 1)} бум.')
        else:
            print(f'За {int((max(inp) * len(inp) - sum(inp)) / 2)} ходов по {(max(inp))} бумажек')


def task2():
    pass

# ============================================     MAIN     ===========================================================


class DStr(str):
    def __init__(self, a):
        self.a = a

    def __sub__(self, b):
        return self.a[len(b):] if self.a.startswith(b) else self.a


def main():
    # d = DStr('1aaaa')
    # b = DStr('1')
    # print(d - b)
    # print(dir(d))
    # task1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    # url = 'https://stepik.org/media/attachments/lesson/254899/menu.json'
    # resp = requests.get(url)
    # resp.encoding = 'utf-8'
    # if resp.status_code == 200:
    #     print(resp.text)
    # else:
    #     print(f'Упс, произошла ошибка!..\nКод ошибки - {resp.status_code}')

    # print(dir(os.path))

    # url = 'https://oeis.org/search'
    # params = {
    #     'q': 631764,
    #     # 'q': 1234567890123456789,
    #     'fmt': 'json'
    # }
    # resp = requests.get(url, params=params)
    # if resp.status_code == 200:
    #     data = resp.json()
    #     count = data['count']
    #     if count == 0:
    #         print('No result')
    #     else:
    #         print(f'\nНайдено {count} последовательностей:\n')
    #         for i in range(len(data['results'])):
    #             print('    {}) № {} - http://oeis.org/A{}'.format(i+1,
    #                                                               data['results'][i]['number'],
    #                                                               data['results'][i]['number']))
    #             print('    Name: {}'.format(data['results'][i]['name']))
    #             print('    Data: {}'.format(data['results'][i]['data']) + '\n')
    #
    #         # json_str = json.dumps(data, indent=4)
    #         # print(json_str)
    # else:
    #     print(f'Ошибка - {resp.status_code}')

    sns.set()
    df = pd.read_csv('tips.csv')
    sns.pairplot(df)


if __name__ == '__main__':
    main()



