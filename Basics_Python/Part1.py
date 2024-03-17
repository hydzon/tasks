"""
1) Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

2) Реализуйте программу, которая будет вычислять количество различных объектов в списке.

3) Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента
целое число x и возвращающую самое маленькое целое число y, такое что:
 - y больше или равно x
 - y делится нацело на 5

 4) Реализуйте программу, которая для заданных n и k вычисляет C(n, k) - число сочетаний из n по k.

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

# ============================================     MAIN     ===========================================================


def main():
    # print(Counter([1, 2, 1, 2, 3, True, 'wef']))
    # assert task2([1, 2, 1, 2, 3]) == 3
    # assert task2([1, 2, 1, 2, 3, True]) == 4
    # print(task3(123))

    print(task4(10, 5))


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
