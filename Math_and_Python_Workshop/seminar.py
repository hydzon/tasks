"""
1) Сколько слов имеют одинаковые первый и последний сомволы?

2) Отсортировать список так, чтобы сначала сначала шли все слова на X, а потом все остальные

3) Отсортировать список кортежей по пследнему элементу из каждого кортежа

4) Напишите функцию fib(n), возвращающую n-е число Фибоначчи.

5) Напишите функцию is_prime(n), проверяющую простое ли число. Если число простое, функция должна вернуть True,
иначе False (логическое значение, не строку!).

6) Считайте строку, содержащую натуральное число - число пончиков
Напишите функцию, принимающую на вход число пончиков, а возвращающую строку:
"Всего пончиков: <число>", если пончиков не больше 9
"Всего пончиков: много", если пончиков больше 9
Выведите на печать результат работы функции для считанного числа пончиков.

7) Напишите функцию, которая принимает на вход строку, а возвращает 2 первых и 2 последних символа.
Если длина исходной строки меньше 2 символов, необходимо вернуть пустую строку.
Выведите на печать результат работы вашей функции, применённый к считанной строке.

8)Напишите функцию, принимающую на вход строку, находящую 1й символ
и заменяющую все его вхождения в строку кроме 1 на *.
Выведите на печать результат работы вашей функции, применённый к считанной строке.

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


def fib(n):
    list_fib_num = [0, 1]
    for i in range(2, n + 1):
        list_fib_num.append(list_fib_num[i - 1] + list_fib_num[i - 2])
    return list_fib_num[-1]


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_modern(n):
    if n == 2:
        return [True, True, True]
    else:
        list_prime_num = is_prime_modern(n - 1)
        for i in range(2, len(list_prime_num)):
            if list_prime_num[i] and n % i == 0:
                list_prime_num.append(False)
                return list_prime_num
    list_prime_num.append(True)
    return list_prime_num

# ============================================     MAIN     ===========================================================


def main():
    print(task1(['apple', 'banana', 'aherre', 'a', 'foasf', 'lowrgn4334i80gvfdn', 'a094ngne', 'fomoi320md']))
    print(task2(['apple', 'foasf', 'Xfsd;ljk', 'lowrgn4334i80gvfdn', 'a094ngne', 'fomoi320md', 'x;ojdfdf']))
    print(task3([(1, 3), (4, 3, 0), (9, 5, 1)]))
    print(fib(12))

    print(is_prime(17))
    print(is_prime_modern(990)[-1])


if __name__ == '__main__':
    main()
