# Задача 4
# Показать первую цифру дробной части числа

a = float(input("Введите дробное число: "))
b = a * 10
b %= 10
print('Первая цифра дробной части:', int(b))
