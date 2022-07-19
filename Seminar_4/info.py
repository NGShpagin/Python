# Записать в файл все числа от 0 до числа, заданного пользователем

# my_num = int(input('Введите число: '))

# with open('test.txt', 'a', encoding='utf-8') as file:
#     # file.write('hello, world!')
#     for i in range(0, my_num+1):
#         file.write(f'\n{str(i)}')

# нежелательный для использования метод
# file = open('test.txt', 'a', encoding='utf-8')
# file.write('hello!')
# file.close()

n = int(input('Введите число: '))
spisok = list(range(n+1))

with open('test.txt', 'w') as file:
    for i in spisok:
        file.write(f'{str(i)}\n')

# with open('test.txt', 'r') as file:
#     a = file.read()
#     print(a)

# with open('test.txt', 'r') as file:
#     for i in range(n):
#         a = file.readline()
#         print(a)

# with open('test.txt','r') as file:
#     k = len(file.readlines())
#     file.seek(0)
#     for i in range(k):
#         a = file.readline()
#         print(a, end = '')

with open('test.txt', 'r') as file:
    read_file = file.read()
    list_of_rows = read_file.split()
print(list_of_rows)

list_of_rows = list(map(int, list_of_rows))

# for i in range(len(list_of_rows)):
#     list_of_rows[i] = int(list_of_rows[i])

print(list_of_rows)
