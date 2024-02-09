import file_tasks
import seminar
import dz_seminar


def test_task1():
    assert seminar.task1(['apple', 'banana', 'aherre', 'a', 'foasf', 'lowrgn4334i80gvfdn', 'a094ngne', 'fomoi320md']) == 1


def test_task2():
    assert file_tasks.task2('sheet1.txt') == 'CONTENT'
    assert seminar.task2(['apple', 'banana', 'aherre', 'a', 'foasf', 'Xfsd;ljk', 'lowrgn4334i80gvfdn', 'a094ngne',
                          'fomoi320md', 'x;ojdfdf']) == ['Xfsd;ljk', 'x;ojdfdf', 'apple', 'banana', 'aherre', 'a',
                                                         'foasf', 'lowrgn4334i80gvfdn', 'a094ngne', 'fomoi320md']


def test_task3():
    assert file_tasks.task3('Привет, мир!') == 'MESSAGE SAVED'
    assert seminar.task3([(1, 3), (4, 3, 0), (9, 5, 1)]) == [(4, 3, 0), (9, 5, 1), (1, 3)]


def test_task4():
    assert file_tasks.task4('output.txt', 'событие') == 'событие записано'


def test_dz_seminar():
    assert dz_seminar.even_indeces([1, 1, 2, 3, 5, 8, 13, 21, 34]) == [1, 2, 5, 13, 34]
    assert dz_seminar.even_elements([1, 1, 2, 3, 5, 8, 13, 21, 34]) == [2, 8, 34]

