"""
На вход программа получает 1 строку - длину ребра додекаэдра.
Нйдите площадь поверхности и объём фигуры.
Ответ округлите до 2 знака после запятой.

"""


def s_dodecahedron(a):
    coef = 3 * (5 * (5 + 2 * 5**0.5))**0.5
    return round(coef * a**2, 2)


def v_dodecahedron(a):
    coef = (15 + 7 * 5**0.5) / 4
    return round(coef * a**3, 2)


def test_s_dodecahedron():
    assert s_dodecahedron(1) == 20.65
    assert v_dodecahedron(1) == 7.66

    assert s_dodecahedron(2) == 82.58
    assert v_dodecahedron(2) == 61.3

