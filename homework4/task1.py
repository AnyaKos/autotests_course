# Напишите функцию which_triangle(a, b, c),
# На вход поступают длины трёх сторон треугольника: a, b, c
# Программа выводит какой это треугольник type_triangle: "Равносторонний", "Равнобедренный", "Обычный".
# Либо "Не треугольник", если по переданным параметрам невозможно построить треугольник
# Например 1, 1, 1 --> "Равносторонний"

def which_triangle(a, b, c):
    """
    Получить тип треугольника по длинам его сторон
    :param a: Длина 1-ой стороны трегольника
    :param b: Длина 2-ой стороны треугольника
    :param c: Длина 3-ей стороны треугольника
    :return: (type_triangle) Тип треугольника
    """
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        type_triangle = "Не треугольник"
    else:
        if (a == b) and (b == c):
            type_triangle = "Равносторонний"
        elif (a == b) or (a == c) or (b == c):
            type_triangle = "Равнобедренный"
        else:
            type_triangle = "Обычный"
    return type_triangle

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]


for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')