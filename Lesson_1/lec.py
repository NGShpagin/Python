# print('Hello world')

# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 213421
# print(type(value))
# s = "hello world"
# print(s)
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, ' + ', b, ' = ', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции

# a = 3.234
# b = 5
# c = round(a * b, 2)
# print(c)

# Логические операции

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции if, else, for

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(f'max =', a)
# else:
#     print(f'max =', b)

# username = input('Введите Ваше имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Ура, это же Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ!')
# else:
#     print('Привет', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i**2)


# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwe - rty':
#     print(i)

# Немного о строках
# text = 'съешь еще этих мягких французских булок'
# print(len(text))
# print('еще' in text)
# print(text.isdigit())               # все символы в строке - числа - False
# print(text.islower())               # все ли символы в строке нижнего регистра - True
# print(text.replace('еще', 'ЕЩЕ'))
# print(text[0])
# print(text[-5])
# print(text[:])                         # вывод всех элементов от 0 до -1
# print()

# Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)

# for e in colors:
#     print(e*2)  # redred greengreen blueblue

# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') # удалить элемент red 

# Функции

# def function_name(x):
    # body line 1
    # ...
    # body line n
    # optional return

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2
# print(f(arg))
# print(type(f(arg)))