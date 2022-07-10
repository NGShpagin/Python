# Найти факториал числа

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

num = int(input('Введите число: '))
print(f'Факториал числа {num}:', factorial(num))