# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

path = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Seminar_4/fileADT2.txt'

# with open(path, 'a') as file:
#      file.write('1 2 3 5 6 7 8')

my_list = []
with open(path, 'r') as file:
    a = file.read()
    print('Числа в файле:', a)
    for i in a:
        if i.isdigit() == True:
            my_list.append(int(i))
    print('Полученный список из чисел файла:', my_list)

for i in range(1, len(my_list)):
    if my_list[i]-1 != my_list[i-1]:
        print('Пропущенное число:', my_list[i]-1)