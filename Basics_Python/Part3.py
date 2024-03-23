"""
1) Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
или Impossible, если операций потребуется более 1000.

2)

"""


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


# ============================================     MAIN     ===========================================================


def main():
    # print(__doc__)
    # s, a, b = input(), input(), input()
    # task1(s, a, b)

    s = "aabaaa"
    t = "aa"
    task2(s, t)


if __name__ == '__main__':
    main()

