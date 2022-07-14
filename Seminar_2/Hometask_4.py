# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число. (Ввести с клавиатуры)

my_list = []
number = int(input('Введите кол-во элементовв списке: '))
while len(my_list) < number:
    num = int(input(f'Введите значения в промежутке от {-number} до {number}: '))
    if (-number) <= num <= number:
        my_list.append(num)
    else:
        print(f'Значение {num} не входит в указанный промежуток')
result = 1
for i in my_list:
    result *= i
print('Список:', my_list)
print('Произведение всех элементов в списке:', result)