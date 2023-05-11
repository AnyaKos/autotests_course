# Напишите функцию flatten_and_sort, которая принимает двумерый массив (список списков) array,
# и возвращает "плоский" список со всеми числами в порядке возрастания result_list
# Например (Ввод --> Вывод) :
#
# [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]] -->  [1, 2, 3, 4, 5, 6, 7, 8, 9]


def flatten_and_sort(array):
    """
    Преобразовать двумерный массив в "плоский" список со всеми числами в порядке возрастания
    :param array: Двумерный массив
    :return: (result_list) "Плоский" список со всеми числами в порядке возрастания
    """
    result_list = []
    for k in array:
        for j in k:
            result_list.append(j)
    result_list.sort()
    return result_list

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]],
    [[], []],
    [[], [1]],
    [[1, 3, 5], [100], [2, 4, 6]]
]

test_data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9], [], [1], [1, 2, 3, 4, 5, 6, 100]
]


for i, d in enumerate(data):
    assert flatten_and_sort(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')