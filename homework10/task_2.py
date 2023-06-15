# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_positive_1():
    assert all_division(135, 5, 3) == 9


def test_positive_2():
    assert all_division(220, 5, 11, 4) == 1


def test_positive_3():
    assert all_division(840, 2, 1, 21, 10) == 2


@pytest.mark.smoke
def test_str():
    with pytest.raises(TypeError):
        all_division(12, '20', 6)


def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(98, 2, 0)
