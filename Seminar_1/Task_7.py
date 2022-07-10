# Задача 7
# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
# if -(a + b + c) == -a*-b*-c:
#     print(True)
# else:
#     print(False)

for x in True, False:
    for y in True, False:
        for z in True, False:
            if not(x or y or z) == (not x and not y and not z):
                print(f'{x =}, {y =}, {z = }')