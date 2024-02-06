"""
1) На вход подаётся строка из целых чисел, разделенных пробелами.
Найдите сумму чисел.


2) Считайте 2 строки. Каждая строка содержит по 3 натуральных числа.
Найдите сумму чисел в каждой строке и выведите на печать одной строкой.
В качестве разделителя между двумя получившимися числами используйте символ "#"

3) На вход подаётся 1 строка, слова в которой разделены символом "&".
Необходимо вывести все слова из строки (без дубликатов) с пробелом в качестве разделителя.

4) На вход подаётся строка, слова в которой разделены между собой пробелами.
Напечатайте 2, 3 и предпоследнее слова из строки (через пробел)

5)На вход подаётся 1 строка, слова в которой разделены пробелами.
Напечатайте слова из этой строки в обратном порядке, используя в качестве разделителя "-$-"

6)На вход подаётся 1 строка, слова в которой разделены пробелами.
Напечатайте через пробел число слов в строке и число слов "one" в строке.
Примечание1. Учитывайте вхождение только слова полностью в нижнем регистре - "one". "One", "ONE" и т.п. не учитывайте.
Примечание2. Число элементов списка L можно получить с помощью конструкции len(L)


7)
Считайте 1 строку. Она содержит строку с названием типа последующих данных. Возможны 3 типа:
int
str
list
В случае получения другого типа выведите на печать строку "Unknown type".

Если получен тип 'int':
Считайте ещё 2 строки. Каждая будет содержать целое число.
Если оба числа равны 0, выведите на печать строку "Empty Ints"
Иначе выведите на печать сумму этих чисел

Если получен тип 'str':
Считайте ещё 1 строку.
Если строка пустая, выведите на печать строку "Empty String"
Иначе напечатайте эту строку

Если получен тип 'list':
Считайте 1 строку и разрежьте её на элементы с помощью split().
Если получившийся список пустой, выведите на печать строку "Empty List"
Иначе выведите на печать последний элемент списка.
"""
# ============================================     task 1-5  ===========================================================

def get_sum(s):
    nums = [int(el) for el in s.split(' ')]
    return sum(nums)


def get_sum2(s1, s2):
    nums1 = map(int, s1.split(' '))
    nums2 = map(int, s2.split(' '))
    return '#'.join([str(sum(nums1)), str(sum(nums2))])


def rem_dubles(s1):
    s1 = set(s1.split('&'))
    return ' '.join(list(s1))


def task4(s1):
    s1 = list(s1.split(' '))
    return ' '.join([s1[1], s1[2], s1[-2]])


def task5(s1):
    s1 = s1.split(' ')[::-1]
    return '-$-'.join(s1)

# ============================================     task 6-..  ==========================================================

def task6(s1):
    s1 = s1.split(' ')
    return str(len(s1)) + ' ' + str(s1.count('one'))


def task7(type_s, s1='', s2=''):
    if type_s == 'int':
        if not int(s1) and not int(s2):
            return "Empty Ints"
        else:
            return int(s1) + int(s2)
    elif type_s == 'str':
        if s1:
            return s1
        else:
            return "Empty String"
    elif type_s == 'list':
        s1 = s1.split()
        if s1:
            return s1[-1]
        else:
            return "Empty List"
    else:
        return "Unknown type"


# ============================================     MAIN     ===========================================================


def main():
    print('START')


if __name__ == '__main__':
    main()


# ============================================     TESTS     ===========================================================


def test_get_sum():


    assert get_sum('1 2 3') == 6


def test_get_sum2():
    assert get_sum2('1 2 3', '1 2 3') == '6#6'


def test_task4():
    assert task4('Some Short String') == 'Short String Short'
    assert task4('And this is some long line, which consists of a set of words') == 'this is of'


def test_task5():
    assert task5('one two three four five six') == 'six-$-five-$-four-$-three-$-two-$-one'


def test_task6():
    assert task6('One string short and one long') == '6 1'
    assert task6('one cat and one dog are friends') == '7 2'


def test_task7():
    assert task7('dict') == 'Unknown type'
    assert task7('int', '0', '0') == 'Empty Ints'
    assert task7('int', '1', '2') == 3
    assert task7('str', 'Hello, World!') == 'Hello, World!'
    assert task7('str', '') == 'Empty String'
    assert task7('list', '1 2 3 4 5') == '5'
    assert task7('list', '') == 'Empty List'
