# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import pytest


@pytest.mark.usefixtures('time_fix_2')
class Test_time:
    def test_time_1(self):
        assert 1 == 1

    def test_time_2(self, time_fix_1):
        assert 2 == 2