# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число: '))
my_list = []


def mnog(num):
    if num == 2:
        my_list.append(num)
    else:
        for i in range(2, num):
            if num % i == 0:
                # print(f'Число не является протым: {num} / {i} =', int(num / i))
                break
            elif i == num-1:
                my_list.append(num)
                # print(f'Число {num} является простым')


for i in range(2, num):
    if num % i == 0:
        mnog(i)

result = 1
new_list = []
while result < num:
    for i in my_list:
        if result * i > num:
            continue
        elif result * i <= num:
            result *= i
            new_list.append(i)


print(f'Список простых множителей числа {num}:', my_list)
print('Итог:', new_list[0], end='')
for i in range(1, len(new_list)):
    print(f' * {new_list[i]}', end='')
print(' =', result)
