# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


alphabet = 'abcdifghijklmnopqrstuvwxyz'


def generate_random_name():
    """Генерирует два слова из латинских букв от 1 до 15 символов"""
    while True:
        a = ((''.join(random.sample(alphabet, random.randint(1, 15)))), ' ', (''.join(random.sample(alphabet, random.randint(1, 15)))))
        yield ''.join(a)


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
