# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.



# Вариант реалиации 1

number = int(input('Введите любое число больше 0: '))
result = 1
index = 1
while index <= number:
    result *= index
    print(result, end=' ')
    index += 1
print()

# Вариант реализации 2 (список)

# number = int(input('Введите любое число больше 0: '))
# my_list = [1]
# index = 2
# while len(my_list) < number:
#     my_list.append(my_list[-1] * index)
#     index += 1
# print(my_list)