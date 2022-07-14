# Найти наибольший простой делитель числа

num = int(input('Введите число: '))
max_div = -1
for i in range(2, num-1):
    if num % i == 0:
        max_div = i
if max_div == -1:
    print(f'число {num} является простым числом')
else:
    print(f'Наибольший делитель для числа {num}: {max_div};   {num} / {max_div} = {int(num / (max_div))}')