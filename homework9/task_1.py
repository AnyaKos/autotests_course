# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


input_file = open("test_file/task1_data.txt", 'r', encoding='utf-8')
output_file = open("test_file/task1_answer.txt", 'w', encoding='utf-8')
for k in input_file:
    for j in k:
        if j.isdigit():
            continue
        else:
            output_file.write(j)
input_file.close()
output_file.close()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
