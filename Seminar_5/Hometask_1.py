# Домашнее задание. Здаача 1
# Напишите программу, удаляющую из текста все слова, содержащие "абв".


string = 'абварк, рапка длырп рыапабв некц авбруг.'


my_list = string.split()
my_list1 = [i for i in my_list if 'абв' not in i]


result_str = ' '.join(my_list1)
print(result_str)
print(*my_list1)