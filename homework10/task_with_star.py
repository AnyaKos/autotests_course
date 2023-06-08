# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    mark = request.node.get_closest_marker('id_check')
    assert mark.args != (), 'Не переданы аргументы'
    print(f'\nПереданы аргументы {mark.args}')
