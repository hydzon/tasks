import file_tasks
import seminar


def test_task1():
    assert seminar.task1(['apple', 'banana', 'aherre', 'a', 'foasf', 'lowrgn4334i80gvfdn', 'a094ngne', 'fomoi320md']) == 1


def test_task2():
    assert file_tasks.task2('sheet1.txt') == 'CONTENT'


def test_task3():
    assert file_tasks.task3('Привет, мир!') == 'MESSAGE SAVED'


def test_task4():
    assert file_tasks.task4('output.txt', 'событие') == 'событие записано'