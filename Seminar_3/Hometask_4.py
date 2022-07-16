# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def transform(num):
    new_string = ''
    result = ''
    print(f'Число {num} в двоичной системе:', end=' ')
    while num > 0:
        new_string += str(num % 2)
        num //= 2
    for i in range(len(new_string)):
        result += new_string[-(i+1)]
    return result


print(transform(45))
print(transform(3))
print(transform(2))
