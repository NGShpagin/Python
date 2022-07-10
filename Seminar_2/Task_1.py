# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def searchNumber(a: int, b: int) -> list:
    my_list = [1]
    while len(my_list) < a:
        my_list.append(my_list[-1]*b)
    return my_list


print(searchNumber(5, -3))


# Второй вариант решения (через цикл for)
# def func(x):
#     s = 1
#     print(s, end=' ')
#     for i in range(1, x+1):
#         s = s*(-3)
#         print(s, end=' ')

# n = int(input('--> '))
# func(n)

# def fun(num = 10, *args, **key):
#     print(args)
#     print(key)

# fun(5, 29, 32, 22, a=1, b=2)
