# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Вариант решения 1

def transform1(num):
    new_string = ''
    result = ''
    print(f'Число {num} в двоичной системе:', end=' ')
    while num > 1:
        new_string += str(num % 2)
        num //= 2
    new_string += str(num)
    for i in range(len(new_string)):
        result += new_string[-(i+1)]
    return result


# Вариант решения 2
def transform2(num):
    num = int(input('Введите число = '))
    my_list = []
    while num > 1:
        new_num = num % 2
        num = num // 2
        my_list.append(new_num)
    my_list.append(num)
    for i in range(len(my_list)):
        print(my_list[-(i + 1)], end='')


print(transform(45))
print(transform(3))
print(transform(2))
