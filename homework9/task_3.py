# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases
a = []
amount = 0
with open("test_file/task_3.txt", "r", encoding='utf-8') as purchases:
    for i in purchases:
        if i != "\n":
            amount += int(i)
            continue
        a.append(amount)
        amount = 0

a.sort(reverse=True)
three_most_expensive_purchases = a[0] + a[1] + a[2]

assert three_most_expensive_purchases == 202346
