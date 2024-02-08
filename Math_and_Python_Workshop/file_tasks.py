"""
1)....считать данные по всем студентам из файла, вычислить средний балл и сравнить его с тем,
что указал преподаватель в mean.


2)На вход подаётся полный путь к файлу относительно текущего каталога.
Проверьте есть ли такой файл (и файл ли это) и если он есть - выведите содержимое. Иначе выведите одну из 2 ошибок.


3)Считайте строку, подаваемую на вход и запишите её в файл "output.txt".
!!!! Если файл уже существует, то открытие его с флагом "w" приведёт к полному уничтожению содержимого при новой записи.
Открытие с флагом "a" позволяет дописывать новые строки в конец файла. !!!!!


4)
event - переменная с текстом события
file_name - имя файла с логом

Файл с логом содержит записи о некоторых событиях
event 3 - 'git log -2'
event 2 - 'git log'
event 1 - 'git status'

Дополните лог в файле так, чтобы новое событие было записано вверху. Не забудьте указать порядковый номер события.
Если файл отсутствует или не содержит записей, начните нумеровать события с 1.
"""


# ============================================     tasks  ===========================================================
import os.path


def task1(file_name):
    f = open(file_name, 'r', encoding="utf-8")
    lines = list(map(lambda x: x.strip('\n').split(), f.readlines()))
    s = sum([int(el[-2]) for el in lines if el[-2].isdigit()])
    print(s)


def task2(file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'r', encoding="utf-8") as f:
            mes = f.read()
            return 'CONTENT'
    elif os.path.exists(file_name):
        print('ERROR:')
        print('Это каталог, а не файл')
    else:
        print('ERROR:')
        print('Файл не существует')


def task3(message):
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(message)
        return 'MESSAGE SAVED'


def task4(log_file, event):
    if os.path.isfile(log_file):
        with open(log_file, 'r', encoding="utf-8") as f:
            old_events = f.readlines()
            count_events = len([el for el in old_events if len(el) > 1])
        with open(log_file, 'w', encoding='utf-8') as f:
            w_event = 'event ' + str(count_events + 1) + ' - ' + event
            f.write(w_event + '\n')
            f.writelines(old_events)
            return 'событие записано'
    else:
        with open(log_file, 'w', encoding='utf-8') as f:
            w_event = r'event 1 - ' + event
            f.write(w_event + '\n')
            return 'событие записано'


# ============================================     MAIN     ===========================================================


def main():
    i = 0
    task1('sheet1.txt')
    task4('output.txt', 'событие')


if __name__ == '__main__':
    main()

