"""
1) На столе лежат n кучек (n > 2) в каждой из которых какое-то кол-во бумажек.
Разрешается за 1 ход игры добавить к 2 любым кучкам по 1 бумажке.
Можно ли по правилам игры уравнять число бумажек в кучках?

Показать минимальное число ходов за которое можно уравнять число бумажек.




"""

import numpy as np
import requests
import os

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


    print(dir(os.path))


if __name__ == '__main__':
    main()



