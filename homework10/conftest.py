import pytest
import datetime


@pytest.fixture
def time_fix_1():
    start = datetime.datetime.now()
    yield start
    print(f'Начало: {start} Окончание: {datetime.datetime.now()}')


@pytest.fixture
def time_fix_2():
    start = datetime.datetime.now()
    yield start
    print(f'Время выполнения: {datetime.datetime.now() - start}')
