"""
Даны длины 2 диагоналей ромба (каждая с новой строки).
Значения могут быть дробными.

Найдите площадь ромба S. В качестве ответа запишите (каждое с новой строки) следующие значения:
S, приведённое к целочисленному типу
S, округлённое до 1 знака после запятой с помощью функции  round()
S, точное значение без округления

"""
x = 2
y = 10


def s_rhombus(a, b):
    return a * b / 2


print(int(s_rhombus(x, y)))
print(round(s_rhombus(x, y), 1))
print(s_rhombus(x, y))

def test_s_rhombus():
    assert s_rhombus(2, 10) == 10.0
    assert s_rhombus(3.6, 7.6) == 13.68