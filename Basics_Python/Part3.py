"""
1) Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
или Impossible, если операций потребуется более 1000.

2) Выведите одно число – количество вхождений строки t в строку s.

3) Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

4) Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

5) Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

6) Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

"""

import sys
import re


# ============================================     tasks 1-2   =========================================================


def task1(s: str, a: str, b: str):
    count, rep_count = 0, 0
    for i in range(1000):
        if a in s:
            new_s = s.replace(a, b)
            if new_s != s:
                rep_count += 1
                s = new_s
            else:
                count += 1
        else:
            if i == 0:
                break
            else:
                count += 1
    return print(rep_count) if count < 1000 and rep_count < 1000 else print('Impossible')


def task2(s: str, t: str):
    return print(len([True for i in range(len(s)) if s[i:].startswith(t)]))


def task3():
    for line in sys.stdin:
        line = line.rstrip()
        if re.findall(r'cat{,2}', line):
            print(line)


def task4():
    for line in sys.stdin:
        line = line.rstrip()
        re_obj = re.search(r'\bcat\b', line)
        if re_obj:
            print(line)


def task5():
    for line in sys.stdin:
        line = line.rstrip()
        re_obj = re.search(r'z\w\w\wz', line)
        if re_obj:
            print(line)


def task6():
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(r'\b(\w+)\1\b', line):
            print(line)

# ============================================     MAIN     ===========================================================


def main():
    # print(__doc__)
    # s, a, b = input(), input(), input()
    # task1(s, a, b)

    # s = "aabaaa"
    # t = "aa"
    # task2(s, t)

    # task3()
    # task4()
    # task5()
    # print(re.match(r'\bcat\b', 'cat cat cat'))



if __name__ == '__main__':
    main()

