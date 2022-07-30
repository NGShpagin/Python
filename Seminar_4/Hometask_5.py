# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


path1 = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Seminar_4/fileHT5_1.txt'
path2 = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Seminar_4/fileHT5_2.txt'
path3 = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Seminar_4/fileHT5_3.txt'

# Каждый знак в многочлене записывается через пробле, кроме возведения в степень x

with open(path1, 'w') as file:
    file.write('7 * x**5 - 6 * x**3 - 7 * x**2 + 18 * x + 2') 
    file.write('9 * x**5 + 9 * x**3 + 4 * x**2 - 5 * x + 3')


with open(path1, 'r') as file1, open(path2, 'r') as file2:
    a = file1.read().split()
    b = file2.read().split()


def create_dict(string: str) -> dict:
    my_dict = {}
    for i in range(len(string)):
        if i == 0 and string[i].count('x'):
            my_dict[string[i]] = 1
        elif i == 1 and string[i].count('x') and string[i-1] == -1:
            my_dict[string[i]] = -1
        elif a[i].count('x'):
            if (i-3 in range(len(string))) and string[i-3] == '-':
                my_dict[string[i]] = -1*int(string[i-2])
            elif (i-2 in range(len(string))) and string[i-2].isdigit() == False:
                if string[i-1] == '-':
                    my_dict[string[i]] = -1
                elif string[i-1] == '+':
                    my_dict[string[i]] = 1
            else:
                my_dict[string[i]] = int(string[i-2])
        elif string[i].isdigit() and ((i+1 in range(len(string)) and string[i+1] != '*') or i == len(string)-1):
            my_dict['num'] = int(string[i])
    return my_dict


def sum_dict(dict1: dict, dict2: dict) -> str:
    string = ''
    for key in dict1.keys():
        if key in dict2.keys():
            if dict1[key] + dict2[key] == 0:
                continue
            elif dict1[key] + dict2[key] == 1 and key != 'num':
                string += f' + {key}'
            elif key == 'num':
                string += f' + {str(dict1[key] + dict2[key])}'
            else:
                string += f' + {str(dict1[key] + dict2[key])} * {key}'
        else:
            if dict1[key] == 1:
                string += f' + {key}'
            if dict1[key] == -1:
                string += f' - {key}'
            else:
                string += f' + {str(dict1[key])} * {key}'
    for key in dict2.keys():
        if key in dict1.keys():
            continue
        else:
            if key == 1:
                string += f' + {str(dict2[key])}'
            else:
                string += f' + {str(dict2[key])} * {key}'
    for i in range(len(string)):
        if (i == 0 or i == 1) and (string[i] == '+' or string[i] == '-'):
            string = string[3:]
    new_string = string.replace(' + -', ' - ')
    return new_string


my_dict1 = create_dict(a)
my_dict2 = create_dict(b)


with open(path3, 'w') as file3:
    file3.write(sum_dict(my_dict1, my_dict2))


print(my_dict1)
print(my_dict2)
print(sum_dict(my_dict1, my_dict2))
