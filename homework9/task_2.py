# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time


def func_log(file_log='log.txt'):
    """
    Декоратор, дозаписывает в файл имя вызываемой функции
    :param file_log: Путь до файла
    :return: Результат дозаписи в файл
    """
    def logs(func):
        """
        Обертка выполняемой функции
        :param func: Функция
        :return: Результат выполнения функции
        """
        def wrapper(*args, ** kwargs):
            """
            Дозаписывает в файл имя вызываемой функции, дату и время вызова по фармату
            :param args: Позиционные аргументы функции
            :param kwargs: Именованные аргументы функции
            :return: Результат выполнения функции
            """
            with open(file_log, "a", encoding="utf-8") as file:
                datetime_now = datetime.datetime.now().strftime("%d.%m %H:%M:%S")
                file.write(f'{func.__name__} вызвана {datetime_now}\n')
            return func(*args, ** kwargs)
        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__
        wrapper.__wrapped__ = func
        return wrapper
    return logs


@func_log()
def func1():
    """Выводит одинаковый текст, когда есть декоратор на функции и когда его нет"""
    time.sleep(3)


@func_log(file_log='func2.txt')
def func2():
    """выводит одинаковый текст, когда есть декоратор на функции и когда его нет"""
    time.sleep(5)


def func_with_star():
    """выводит одинаковый текст, когда есть декоратор на функции и когда его нет"""
    time.sleep(2)

func1()
func2()
func1()

help(func1)
