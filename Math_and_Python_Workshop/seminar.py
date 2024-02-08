"""
1) Сколько слов имеют одинаковые первый и последний сомволы?


"""


# ============================================     tasks  ===========================================================
def task1(words):
    count = 0
    for word in words[:-2]:
        if word[0] == word[-1] and len(word) > 1:
            count += 1
    return count


# ============================================     MAIN     ===========================================================

def main():
    print(task1(['apple', 'banana', 'aherre', 'a', 'foasf', 'lowrgn4334i80gvfdn', 'a094ngne', 'fomoi320md']))


if __name__ == '__main__':
    main()
