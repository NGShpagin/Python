# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]


path = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Lecture_3/Task1.txt'

# Решение на Лекции

# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]

# out = []

# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))

# print(out)




data = '1 2 3 5 8 15 23 38'.split()

result = map(int, data)
result = filter(lambda x: not x % 2, result)
result = list(map(lambda x: (x, x**2), result))

print(result)
