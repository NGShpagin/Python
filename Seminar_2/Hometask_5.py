# Реализуйте алгоритм перемешивания списка.

from random import randint


my_list = []
number = int(input('Введите кол-во элементовв списке: '))
while len(my_list) < number:
    my_list.append(randint(1,9))
print('Заданный список: ', my_list)
for i in range(0, number):
    cont = my_list[i]
    rand_index = randint(0, number-1)
    my_list[i] = my_list[rand_index]
    my_list[rand_index] = cont
print('Получишийся список: ', my_list)