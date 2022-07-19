# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(n):
    if n == 0:
        return 0
    elif n == -1 or n == 1:
        return 1
    else:
        if n > 0:
            return fib(n-1) + fib(n-2)
        elif n < 0:
            return fib(n+2) - fib(n+1)


def printFib(n):
    my_list = []
    for i in range(-n, n+1):
        my_list.append(fib(i))
    return my_list


print(printFib(8))