# Задача 2
# Найти максимальное из пяти чисел

numbers = [1, 5, 45, 4, 33]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)