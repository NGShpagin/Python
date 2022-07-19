# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число. (Ввести с клавиатуры)

with open('file.txt', 'w') as file:
    indices = input('Введите числа через пробел: ')
    indices = indices.split(' ')
    for el in indices:
        file.write(f'{el}\n')


my_list = []
number = int(input('Введите число: '))
result = 1
for i in range(-number, number+1):
    if i == 0:
        continue
    else:
        my_list.append(i)
with open('file.txt', 'r') as file:
    a = file.read().split()
    for i in a:
        if int(i) in range(len(my_list)):
            result *= my_list[int(i)]
print('Элементы в файле', a)
print('Список:', my_list)
print('Произведение всех элементов в списке:', result)
