# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

class PersonInfo:
    """Обработка персональных данных сотрудника"""
    def __init__(self, name: str, age: int, *args):
        """
        Инициализация класса PersonInfo
        :param name: Строка Имя Фамилия
        :param age: Возраст сотрудника
        :param args: Подразделения от головного до того, где работает сотрудник
        """
        self.name = name
        self.age = age
        self.department = args

    def short_name(self):
        """
        Возвращает строку формата 'Фамилия И.'
        :return: Строка формата 'Фамилия И.'
        """
        first_name = self.name.split(" ")[0]
        last_name = self.name.split(" ")[1]
        return last_name + " " + first_name[0]+"."

    def path_deps(self):
        """
        Возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
        :return: (path) путь "Головное подразделение --> ... --> Конечное подразделение"
        """
        path = ""
        for d in self.department:
            path = path + d
            if d == self.department[len(self.department)-1]:
                break
            path = path + " --> "
        return path

    def new_salary(self):
        """
        Возвращает проиндексированную зарплату
        :return: Зарплата после индексации
        """
        letters_dict = {}
        path = ""
        for k in self.department:
            path = path + k
        for j in path:
            if j in letters_dict.keys():
                letters_dict.update({j: letters_dict.get(j) + 1})
            else:
                letters_dict.setdefault(j, 1)
        letters_dict = dict(reversed(sorted(letters_dict.items(), key=lambda item: item[1])))
        count = 3
        values = 0
        for v in letters_dict:
            values += letters_dict.get(v)
            count -= 1
            if count == 0:
                break
        return 1337*self.age*values

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
