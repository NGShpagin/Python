# Задача 1
# По двум заданным числам проверить является ли одно квадратом второго 

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a**2 == b:
    print(f'{a} в квадрате равно {b}')
else:
    print((f'{a} в квадрате не равно {b}'))