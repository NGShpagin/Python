# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите натуральное число: '))


def check_num(num: int) -> bool:
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            elif i == num-1:
                return True


def create_list(num: int) -> list:
    my_list = []
    for i in range(2, num):
        if num % i == 0:
            if check_num(i) == True:
                my_list.append(i)
            else:
                continue
        else:
            continue
    return my_list


my_list = create_list(num)
new_list = []

if len(my_list) != 0:
    result = num
    while check_num(result) == False or result == 2 or result == 3:
        for i in my_list:
            if result % i == 0:
                result //= i
                new_list.append(i)
            else:
                continue
else:
    print(f'Число {num} - простое')
    exit()

print(new_list)
print(f'Список простых множителей числа {num}:', my_list)
print('Итог:', new_list[0], end='')
for i in range(1, len(new_list)):
    print(f' * {new_list[i]}', end='')
print(' =', num)
