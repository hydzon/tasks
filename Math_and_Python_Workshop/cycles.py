"""
1) Считайте натуральное число n.
Выведите на печать все квадраты чётных чисел от 0 до n-1 (включительно), каждый с новой строки.

2)Считывайте целые числа из потока ввода по одному до тех пор, пока не встретите строку "The End".
Выведите на печать сумму считанных чисел.

3)На вход подаётся строка, некоторые слова в которой "испорчены".
Признак "испорченного" слова - 1я буква в нём заменена на *.
Выведете на печать только "не испорченные" слова, каждое с новой строки

4)Считайте натуральное число n
Найдите самый маленький натуральный делитель числа n, отличный от 1 (2 <= n <= 30000).

"""


# ============================================     task 1-5  ===========================================================

def task1(n):
    u = list()
    for i in range(0, n):
        if i % 2 == 0:
            u.append(i **2)
    return u


def task2():
    istr = ''
    summa = 0
    while not istr == 'The End':
        istr = input()
        if not istr == 'The End':
            summa += int(istr)
    print(summa)
    return summa


def task3(st):
    st = st.split()
    st = [el for el in st if el[0] != '*']
    return st


def task4(n):
    for i in range(2, 30000):
        if n % i == 0:
            return i

# ============================================     MAIN     ===========================================================


def main():
    print('START')
    print(task2())


if __name__ == '__main__':
    main()


# ============================================     TESTS     ===========================================================

def test_task1():
    assert task1(7) == [0, 4, 16, 36]


def test_task3():
    assert task3('exaggeration *romotion run into admit exactly *idelity *erspective treat '
                 'check certain') == ['exaggeration', 'run', 'into', 'admit', 'exactly', 'treat', 'check', 'certain']


def test_task4():
    assert task4(2589) == 3
