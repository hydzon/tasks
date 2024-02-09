"""
1) Сколько слов имеют одинаковые первый и последний сомволы?

2) Отсортировать список так, чтобы сначала сначала шли все слова на X, а потом все остальные

3) Отсортировать список кортежей по пследнему элементу из каждого кортежа

"""


# ============================================     tasks  ===========================================================
def task1(words):
    count = 0
    for word in words[:-2]:
        if word[0] == word[-1] and len(word) > 1:
            count += 1
    return count


def task2(words_list):
    words_list_x = [word for word in words_list if word[0] == 'x' or word[0] == 'X']
    words_list_x += [word for word in words_list if word[0] != 'x' and word[0] != 'X']
    return words_list_x


def task3(tup_list):
    return sorted(tup_list, key=lambda x: x[-1])


# ============================================     MAIN     ===========================================================

def main():
    print(task1(['apple', 'banana', 'aherre', 'a', 'foasf', 'lowrgn4334i80gvfdn', 'a094ngne', 'fomoi320md']))
    print(task2(['apple', 'foasf', 'Xfsd;ljk', 'lowrgn4334i80gvfdn', 'a094ngne', 'fomoi320md', 'x;ojdfdf']))
    print(task3([(1, 3), (4, 3, 0), (9, 5, 1)]))


if __name__ == '__main__':
    main()
