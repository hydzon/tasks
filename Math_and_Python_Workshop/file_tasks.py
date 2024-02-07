"""
1)

"""


# ============================================     tasks  ===========================================================


def task1(file_name):
    f = open(file_name, 'r', encoding="utf-8")
    lines = list(map(lambda x: x.strip('\n').split(), f.readlines()))
    s = sum([int(el[-2]) for el in lines if el[-2].isdigit()])
    print(s)


# ============================================     MAIN     ===========================================================


def main():
    i = 0
    task1('sheet1.txt')


if __name__ == '__main__':
    main()


# ============================================     TESTS     ===========================================================


# def test_task1():
#     assert task1(0) == 1
