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

import csv
import sys
import re
import requests
import json
import numpy as np
import pandas as pd
import datetime
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


def parentage_check(classes, parent, child):
    if classes[child] is None:
        return False
    elif parent in classes[child]:
        return True
    else:
        for i in range(len(classes[child])):
            if parentage_check(classes, parent, classes[child][i]):
                return True
    return False


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
    # text = '''
    #     <a href="https://stepik.org/media/attachments/lesson/24472/sample1.html">1</a>
    #     <a href="http://stepik.org/courses">
    #     <a href='https://stepik.org'>
    #     <a href='http://neerc.ifmo.ru:1345'>
    #     <a href= "ftp://mail.ru/distib" >
    #     <a href="ya.ru">
    #     <a href="www.ya.ru">
    #     <a href="../skip_relative_links">
    #     <a href="../some_path/index.html">
    #     <a href="sas-_0123d.ifmo.ru">
    #     <a target='_top' href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">
    # '''
    # # req = requests.get(input().replace('stepic.org', 'stepik.org'))
    # l_set = set(re.findall(r'(?:<a[ ]*href[ ]*=[ ]*["\'].*?)((?:\w+)(?:[.]\w+){1,})', text))
    # print(*sorted((list(l_set))), sep='\n')

    # req = requests.get('http://pastebin.com/raw/7543p0ns')
    # print(req)
    # # print(*re.findall(r'(?:\w+)(?:[.]\w+){1,}', text), sep='\n')

    # # Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
    # temp_df = pd.read_csv('Crimes.csv', sep=',')
    # temp_df['Date'] = pd.to_datetime(temp_df['Date'])
    # temp_df = temp_df[(temp_df.Date >= pd.Timestamp('01-01-2015')) & (temp_df.Date <= pd.Timestamp('01-01-2016'))]
    # print(temp_df.groupby('Primary Type')['Primary Type'].count().idxmax())


    """
        Вам дано описание наследования классов в формате JSON.
        Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
        <имя класса> : <количество потомков>
        Выводить классы следует в лексикографическом порядке.
    """
    # text = ('[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, '
    #         '{"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]')
    # dict_obj = {el['name']: el['parents'] for el in json.loads(text)}
    # res = dict()
    # for el in sorted(dict_obj):
    #     res[el] = 1
    #     for sub_el in dict_obj:
    #         if parentage_check(dict_obj, el, sub_el):
    #             res[el] += 1
    # for key, value in sorted(res.items()):
    #     print(f'{key} : {value}')

    """
        Получить данные о погоде через API с сайта openweathermap.org            
    """

    # api_url = 'https://api.openweathermap.org/data/2.5/weather'
    # params = {
    #     'id': '2025339',                                    # City ID
    #     'appid': '8358868cc2bddccd3299ff652bd01e2a',        # Key
    #     'lang': 'ru',                                       # Lang
    #     'units': 'metric'                                   # Units of measurement
    # }
    # response = requests.get(api_url, params=params)
    # print(response.json()['main']['temp'])

    """     
        С помошью API сайта numbersapi.com,  
        необходимо узнать, существует ли интересный математический факт о числе.        
        Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
    """

    # api_url = 'http://numbersapi.com'
    # params = {
    #     'json': 'true'
    # }
    #
    # num = input()
    # while num:
    #     response = requests.get(api_url + f'/{num}/math', params=params)
    #     data = response.json()
    #     print('Interesting') if data['found'] else print('Boring')
    #     print(data['text'])
    #     num = input()

    '''
        В этой задаче вам необходимо воспользоваться API сайта artsy.net    
        Вам даны идентификаторы художников в базе Artsy.
        Для каждого идентификатора получите информацию о имени художника и годе рождения.
        Выведите имена художников в порядке неубывания года рождения. В случае если у художников 
        одинаковый год рождения, выведите их имена в лексикографическом порядке.
    '''

    # with open('token_Artsy', 'r') as t:
    #     headers = {"X-Xapp-Token": t.readline()}
    # list_arts = []
    # read = input()
    # while read:
    #     r = requests.get("https://api.artsy.net/api/artists/" + read,
    #                   headers=headers)
    #     r.encoding = 'utf-8'
    #     list_arts.append([json.loads(r.text)['sortable_name'], json.loads(r.text)['birthday']])
    #     read = input()
    # list_arts = pd.DataFrame(list_arts, columns=['artist', 'birthday'])
    # # print(list_arts)
    # list_arts = list_arts.sort_values(by=['birthday', 'artist'])
    # print(list_arts)
    # print(*list_arts['artist'].tolist(), sep='\n')


if __name__ == '__main__':
    main()

