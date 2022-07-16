# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


my_list = [1.1, 1.2, 3.1, 5, 10.01]
max = round(my_list[0] - int(my_list[0]), 2)
min = round(my_list[0] - int(my_list[0]), 2)
for i in my_list:
    if round(i - int(i), 3) == 0:
        continue
    elif round(i - int(i), 3) > max:
        max = round(i - int(i), 2)
    elif round(i - int(i), 3) < min:
        min = round(i - int(i), 2)
result = max - min
print('Max =', max, 'Min =', min)
print('Result =', result)
