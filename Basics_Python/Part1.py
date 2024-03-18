"""
1) Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

2) Реализуйте программу, которая будет вычислять количество различных объектов в списке.

3) Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента
целое число x и возвращающую самое маленькое целое число y, такое что:
 - y больше или равно x
 - y делится нацело на 5

 4) Реализуйте программу, которая для заданных n и k вычисляет C(n, k) - число сочетаний из n по k.

 5) Реализуйте программу, которая будет эмулировать работу с пространствами имен.
 Необходимо реализовать поддержку создания пространств имен и добавление в них переменных

В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины не более 10,
состоящие из строчных латинских букв.

Для каждого запроса get выведите в отдельной строке его результат.


6) Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить
сумму пятерок последовательных элементов по мере их накопления.
"""

# ============================================     tasks 1-5   =========================================================


def task1():
    n = int(input())
    print(sum([int(input()) for _ in range(n)]))


def task2(objects):
    return len(set([id(el) for el in objects]))


def task3(x):
    return x if x % 5 == 0 else x + (5 - x % 5)


def task4(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return task4(n - 1, k) + task4(n - 1,  k - 1)


class NameSpace:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.variables = []

    def add_variable(self, var):
        self.variables.append(var)

    def get_variables(self, var):
        if var in self.variables:
            return self.name
        else:
            if self.parent is None:
                return None
            return self.parent.get_variables(var)


name_space = {'global': NameSpace('global', None)}
get_stack = []


def create_namespace(new_namespaces, parent):
    name_space[new_namespaces] = NameSpace(new_namespaces, name_space[parent])


def add_variables(namespaces, variable):
    name_space[namespaces].add_variable(variable)


def instructions_implementer(cmd, ns, var):
    if cmd == 'create':
        create_namespace(ns, var)
    elif cmd == 'add':
        add_variables(ns, var)
    else:
        get_stack.append((ns, var))


def task5():
    instructions_count = 9
    for _ in range(instructions_count):
        instructions_implementer(*input().split())
    for i in range(len(get_stack)):
        print(name_space[get_stack[i][0]].get_variables(get_stack[i][1]))


# ============================================     tasks 6-10   ========================================================


class Buffer:
    buffer = []

    def __init__(self):
        pass

    def add(self, *a):
        self.buffer.extend(a)
        for i in range(len(self.buffer) // 5):
            print(sum(self.buffer[i * 5: i * 5 + 5]))
        c = len(self.buffer) % 5
        if len(self.buffer) % 5:
            self.buffer = self.buffer[-(len(self.buffer) % 5):]
        else:
            self.buffer = []

    def get_current_part(self):
        return self.buffer


# ============================================     MAIN     ===========================================================


def main():
    # print(Counter([1, 2, 1, 2, 3, True, 'wef']))
    # assert task2([1, 2, 1, 2, 3]) == 3
    # assert task2([1, 2, 1, 2, 3, True]) == 4
    # print(task3(123))
    # print(task4(10, 5))

    task5()
    """
    add global a
    create foo global
    add foo b
    get foo a
    get foo c
    create bar foo
    add bar a
    get bar a
    get bar b
    """

    # buf = Buffer()
    # buf.add(1, 2, 3)
    # print(buf.get_current_part())  # вернуть [1, 2, 3]
    # buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
    # print(buf.get_current_part())  # вернуть [6]
    # buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
    # print(buf.get_current_part())  # вернуть []
    # buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
    # print(buf.get_current_part())  # вернуть [1]


if __name__ == '__main__':
    main()

# def s(a, *vs, b=10):
#     res = a + b
#     for v in vs:
#         res += v
#     print(res)
#
#
# answers = {
#     's(11, 10)', 's(0, 0, 31)', 's(11, b=20)',
#     's(b=31)', 's(11, 10, b=10)', 's(21)',
#     's(b=31, 0)', 's(11, 10, 10)', 's(5, 5, 5, 5, 1)'
# }
#
# for answer in answers:
#     print(f'функция с аргументами: {answer} | вернула:', end=' ')
#     try:
#         exec(answer)
#     except Exception as e:
#         print(f'ошибку "{type(e)}" с пояснением "{e}"')


# def tests_for_task2():
#     assert task2([1, 2, 1, 2, 3]) == 3
#     assert task2([1, 2, 1, 2, 3, True]) == 4
#
#
# def tests_for_task3():
#     assert task3(5) == 5
#     assert task3(17) == 20
#     assert task3(1000) == 1000
#     assert task3(199) == 200
