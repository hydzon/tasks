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

7) В каждой строке замените первое вхождение слова, состоящего
только из латинских букв "a" (регистр не важен), на слово "argh".

8) В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.

9) Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3, не используя приведение к числу.
"""

import sys
import re
import requests
import json

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


def task7():
    for line in sys.stdin:
        line = line.rstrip()
        if re.findall(r'\b[aA]+\b', line):
            print(re.sub(r'\b[aA]+\b', 'argh', line, count=1))


def repl(m):
    return m[0][1]+m[0][0]+m[0][2:]


def task8():
    for line in sys.stdin:
        line = line.rstrip()
        if re.findall(r'\b\w{2,}\b', line):
            print(re.sub(r'\b\w{2,}\b', repl, line))  # re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)


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

    # task8()

    '''
        На вход подаются две строки, содержащие url двух документов A и B.
        Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
    '''

    # a = 'https://stepik.org/media/attachments/lesson/24472/sample0.html'
    # b = 'https://stepik.org/media/attachments/lesson/24472/sample2.html'
    # res = requests.get(a)
    # c = re.findall(r'<a href="(.+)">', res.text)[0]
    # res = requests.get(c)
    # c = re.findall(r'<a href="(.+)">', res.text)[0]
    # c = c.replace('stepic.org', 'stepik.org')
    # print('Yes') if b == c else print('No')


    '''
        На вход подается ссылка на HTML файл.
        Вам необходимо скачать этот файл, затем найти в нем все ссылки 
        вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.   
    '''

    # req = requests.get(input())
    # links = re.findall(r'<a href="(.+)">', req.text)



if __name__ == '__main__':
    main()

