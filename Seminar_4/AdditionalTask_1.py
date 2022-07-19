# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

path = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Seminar_4/fileADT1.txt'

# with open(path, 'a') as file:
#     file.write('\nAlekseev: 42786.98')

def readDict(path: str) -> dict:
    my_dict = {}
    with open(path, 'r') as file:
        a = file.readlines()
        for i in a:
            key = ''
            value = ''
            for k in i:
                if k.isdigit() == True or k == '.':
                    value += k
                elif k == ':':
                    continue
                elif k.isalpha():
                    key += k
            values = float(value)
            my_dict[key] = values
    return my_dict


def minSal(my_dict: dict, salary: int) -> float:
    minSal = []
    for key in my_dict:
        if my_dict[key] < salary:
            minSal.append(key)
    return minSal


my_dict = readDict(path)
print('Величина окладов сотрудников:')
for i, key in enumerate(my_dict):
    print(f'{i+1}. {key}: {my_dict[key]}')

sal = 20000
print(f'\nСотрудники с окладом менее {sal}:')
for i, item in enumerate(minSal(my_dict, sal)):
    print(f'{i+1}. {item}: {my_dict[item]}')

result = 0
for key in my_dict:
    result += my_dict[key]
aver = result / len(my_dict)
print(f'\nСредняя зарплата всех сотрудников:', aver)
