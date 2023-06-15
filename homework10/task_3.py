# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args, result', [([220, 5, 11, 4], 1), pytest.param([135, 5, 3], 9, marks=pytest.mark.smoke)])
def test_positive(args, result):
    assert all_division(*args) == result


@pytest.mark.parametrize('args, result', [pytest.param([98, 2, 0], ZeroDivisionError, marks=pytest.mark.skip('bad data')), ([12, '20', 6], TypeError), ([], IndexError)])
def test_negative(args, result):
    with pytest.raises(result):
        all_division(*args)
