"""
1) В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит,
когда с момента исходной даты date пройдет число дней, равное days.

2) Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
Вам необходимо узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.
Ответом для данной задачи служит расшифрованная интересная информация Алисы.

"""

import datetime
from simplecrypt import encrypt, decrypt

# ============================================     tasks 1-5   =========================================================


def task1():
    date = datetime.date(*map(int, input().split()))
    date += datetime.timedelta(int(input()))
    print(f'{date.year} {date.month} {date.day}')


def task2():
    with open("encrypted.bin", "rb") as inp:
        encrypted = inp.read()
        with open("passwords.txt", "r") as ps_file:
            passwords = [ps[:-1] for ps in ps_file.readlines()]
            print(passwords)
        for el in enumerate(passwords):
            try:
                print(decrypt(el[1], encrypted))
                break
            except Exception as e:
                print(f'Пароль {el[1]} не подошел')


# ============================================     MAIN     ===========================================================


def main():
    # task1()
    task2()


if __name__ == '__main__':
    main()

