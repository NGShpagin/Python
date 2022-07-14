# Задайте список из n чисел последовательности (1 + 1 / n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# number = int(input('Введите число  = ')) 
# sum = 0 
# x = 0 
# my_list = [] 
# print('{', end = ' ') 
# for i in range(1,n + 1): 
#     x = round((1+1/i)**i,2) 
#     print( i,':', x,',',end = ' ') 
#     my_list.append(x) 
#     sum = sum + x 
   
# print ('}') 
# print('Cумма чисел последовательности = ',sum) 
# print(my_list)


num = int(input('Введите число: '))
suc = round((1+ 1/num)**num)
my_list = [1+suc]
sum = 0
while len(my_list) < num:
    my_list.append(my_list[-1]+suc)
for i in my_list:
    sum += i
print(f'Последовательность: (1+1/{num})^{num} = ', (round((1+ 1/6)**6)), '(округлена до целого числа)')
print(my_list)
print('Сумма всех элементов в списке: ', sum)