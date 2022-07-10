# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

str1 = 'напишите программу, в которой ап пользователь будет задавать апдве строки'
str2 = 'ап'

# 1-ый Вариант решения 
index = 0
count = 0
while True:
    index = str1.find(str2, index)
    if index == -1:
        break
    index += 1
    count += 1
print(count)

# 2-ой Вариант решения 
# st1 = 'привет, мир, т, привет!'
# st2 = ','
# def str(st1, st2):
#     count = 0
#     for i in range(len(st1) - len(st2)):
#         if (st1[i : i + len(st2)] == st2):
#             count += 1
#     return count
# print(str(st1, st2))
