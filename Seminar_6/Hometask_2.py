# Домашнее задание. Задача 2
# Задача: предложить улучшения кода для уже решённых задач с 
# помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# Найти сумму чисел списка стоящих на нечетной позиции
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}




my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# Задача 1
result = list(filter(lambda i: my_list.count(i) == 1, my_list)) 

# Задача 2
# data = [my_list[i] for i in range(len(my_list)) if i % 2 == 0] # не по индексу, а по позиции
summa = sum(my_list[i] for i in range(len(my_list)) if i % 2 == 0) 
    
    # 1 Варинта решения
# summa = 0
# for i in data:
#     summa += i
    # 2ой вариант решения
# summa = sum(data)

# summa = 0
# map(lambda x: summa = x, data)

# Задача 3
num = 6
task_list = [i for i in range(1, num+1)]
new_task_list = list(map(lambda i:  3*i + 1, task_list))
my_dict = dict(zip(task_list, new_task_list))

print('Начальный список:', my_list)
print('Задача 1. Список уникальных чисел:', result)
# print('Список значений на нечетных позициях:', data)
print('Задача 2. Сумма всех чисел на нечетных позициях:', summa)
# print(f'Список значений числа {num}:', task_list)
print(f'Задача 3. Полученный словарь из числа {num}:', my_dict)
