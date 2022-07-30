# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта
# и возвращает итератор с новыми объектами
# !Нельзя пройтись дважды!

# li = [x for x in range(1, 21)]
# li = list(map(lambda x: x+10, li))
# print(li)


# data = list(map(int, input().split()))
# print(data)

data = list(map(int, '1 34 876'.split()))

for e in data:
    print(e)

print('--')

for e in data:
    print(e)