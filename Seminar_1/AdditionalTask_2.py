# Проверить число на простоту (т.е. что число делится только на 1 и само на себя)

a = int(input('Введите число: '))
if a % 2 == 0:
    print('a / 2 =', a / 2)
    print(False)
elif a % 3 == 0:
    print('a / 3 =', a / 3)
    print(False)
elif a % 5 == 0:
    print('a / 5 =', a / 5)
    print(False)
elif a % 7 == 0:
    print('a / 7 =', a / 7)
    print(False)
else:
    print(True)