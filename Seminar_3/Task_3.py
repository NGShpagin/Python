# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time

# Вариант решение с range


def find_num(c, d):  # с - от, d - до, условие: размер чисел с и d одинаковый
    b = ''
    a1 = str(c)
    a2 = str(d)
    count = 2
    a = str(time.time())
    while int(a[-1]) < int(a1[0]) or int(a[-1]) > int(a2[0]):
        a = str(time.time())
    b += a[-1]
    while count <= len(a2):
        a = str(time.time())
        if count == len(a2):
            if int(b[-1]) < int(a2[-2]) and int(b[-1]) > int(a1[-2]):
                b += a[-1]
                break
            else:
                while int(a[-1]) > int(a2[-1]):
                    a = str(time.time())
                b += a[-1]
                break
        elif int(b[-1]) < int(a2[count-2]):
            while int(a[-1]) < int(a1[count-1]):
                a = str(time.time())
            b += a[-1]
        else:
            while int(a[-1]) > int(a2[count-1]):
                a = str(time.time())
            b += a[-1]
        count += 1
    return int(b)


print(find_num(220, 317))


# Вариант решения 1

# def find_num(x):
#     a = str(time.time())
#     b = ''
#     count = 1
#     while count <= x:
#         if a[-count] == '.':
#             continue
#         b += a[-count]
#         count += 1
#     return int(b)


# Вариант решения 2

# def find_num(x):
#     b = ''
#     count = 1
#     while count <= x:
#         a = str(time.time())
#         b += a[-1]
#         count += 1
#     return int(b)


# def find_num(c, d): # с - от, d - до
#     b = ''
#     a1 = str(c)
#     a2 = str(d)
#     count = 2
#     a = str(time.time())
#     while int(a[-1]) < int(a1[0]) or int(a[-1]) > int(a2[0]):
#         a = str(time.time())
#     b += a[-1]
#     if int(time.time()) % 2 > 0:
#         my_len = len(a1)
#     else:
#         my_len = len(a2)
#     while count <= my_len:
#         a = str(time.time())
#         if count == my_len:
#             if int(b[-1]) < int(a2[-2]):
#                 b += a[-1]
#                 break
#             else:
#                 while int(a[-1]) > int(a2[-1]):
#                     a = str(time.time())
#                 b += a[-1]
#                 break
#         elif int(b[-1]) < int(a2[count-2]):
#             b += a[-1]
#         else:
#             while int(a[-1]) > int(a2[count-1]):
#                 a = str(time.time())
#             b += a[-1]
#         count += 1
#     return int(b)

# print(find_num(91, 113))


# Варинат решения (Антона)

# l = int(input('Введите длинну числа: '))

# ms = int(((time.time() % 1) * (10 ** (l + 1))) % (10 ** (l)))
# ms = time.time()
# ms = int(time.time() % 10)

# print(ms)
