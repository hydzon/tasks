"""Стандартное (среднеквадратическое) отклонение"""


nums = [2, -1, 2]


def st_dev(nums):
    sr = sum(nums) / len(nums)
    disp = sum([(n - sr) ** 2 for n in nums])/len(nums)
    return disp ** 0.5


def main():
    print(st_dev(nums))


if __name__ == '__main__':
    main()


def test_st_dev():
    assert st_dev([1, 2, 3, 4]) == 1.118033988749895
    assert st_dev([1, 5, 2, 7, 1, 9, 3, 8, 5, 9]) == 3
    assert st_dev([1, 5, 2, 7, 1, 9, 3, 8, 5]) == 2.8327886186626583
    assert st_dev([0]) == 0
