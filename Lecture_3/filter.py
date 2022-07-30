# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта
# и возвращает итеартор с теми объектами, для которых ункция вернула True.
# f(x) = True - нечетное
# filter(f, [1, 2, 3, 4, 5])

data = [x for x in range(10)]
result = list(filter(lambda x: not x % 2, data))
print(result)
