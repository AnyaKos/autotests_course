# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

class RomanNums:
    """Обработка римского числа"""
    def __init__(self, roman: str):
        """
        Инициализация класса RomanNums
        :param roman: Строка с римским числом
        """
        self.roman = roman

    def from_roman(self):
        """
        Переводит римскую запись числа в арабскую
        :return: (number_arab) Арабская запись числа
        """
        roman_dict_reverse = dict(CM=900, CD=400, XC=90, XL=40, IX=9, IV=4)
        roman_dict = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)
        number_arab = 0
        roman_number = self.roman
        for j in roman_dict_reverse.keys():
            if j in roman_number:
                number_arab += roman_dict_reverse.get(j)
                roman_number = roman_number.replace(j, "", 1)
        for k in roman_dict.keys():
            for k in roman_number:
                number_arab += roman_dict.get(k)
                roman_number = roman_number.replace(k, "", 1)
        return number_arab

    def is_palindrome(self):
        """
        Возвращает (True - является, иначе False) является ли арабское число палиндромом
        :return: True - палиндромом, иначе False
        """
        return RomanNums(self.roman).from_roman() == int(str(RomanNums(self.roman).from_roman())[::-1])

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]


test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')