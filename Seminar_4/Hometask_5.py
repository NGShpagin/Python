# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


path1 = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Seminar_4/fileHT5_1.txt'
path2 = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Seminar_4/fileHT5_2.txt'
path3 = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Seminar_4/fileHT5_3.txt'

with open(path1, 'w') as file:
    file.write('7 * x**5 - 6 * x**3 - 7 * x**2 + 18 * x + 2')

with open(path2, 'w') as file:
    file.write('9 * x**5 + 9 * x**3 + 4 * x**2 - 5 * x + 3')


with open(path1, 'r') as file1, open(path2, 'r') as file2, open(path3, 'w') as file3:
    a = file1.read().split()
    b = file2.read().split()
    dict1 = {}
    dict2 = {}
    for i in range(len(a)):
        if i == 0 and a[i].count('x'):
            dict1[a[i]] = 1
        elif i == 1 and a[i].count('x') and a[i-1] == -1:
            dict1[a[i]] = -1
        elif a[i].count('x'):
            if (i-3 in range(len(a))) and a[i-3] == '-':
                dict1[a[i]] = -1*int(a[i-2])
            elif (i-2 in range(len(a))) and a[i-2].isdigit() == False:
                if a[i-1] == '-':
                    dict1[a[i]] = -1
                elif a[i-1] == '+':
                    dict1[a[i]] = 1
            else:
                dict1[a[i]] = int(a[i-2])
        elif a[i].isdigit() and ((i+1 in range(len(a)) and a[i+1] != '*') or i == len(a)-1):
            dict1['num'] = int(a[i])

    for i in range(len(b)):
        if i == 0 and a[i].count('x'):
            dict1[a[i]] = 1
        elif i == 1 and a[i].count('x') and a[i-1] == -1:
            dict1[a[i]] = -1
        elif b[i].count('x'):
            if (i-3 in range(len(b))) and b[i-3] == '-':
                dict2[b[i]] = -1*int(b[i-2])
            else:
                dict2[b[i]] = int(b[i-2])
        if b[i].isdigit() and ((i+1 in range(len(b))) and b[i+1] != '*' or i == len(b)-1):
            dict2['num'] = int(b[i])

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
    file3.write(new_string)


print(dict1)
print(dict2)
print(new_string)
