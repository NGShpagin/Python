# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:*
#         1+2*3 => 7;
#         (1+2)*3 => 9;


def calc(s):
    count = ''
    digit = []
    for i in range(len(s)):
        if s[i].isdigit():
            count += s[i]
        else:
            digit.append(int(count))
            digit.append(s[i])
            count = ''
    digit.append(int(count))
    return digit


def decision(my_list):
    while len(my_list) > 1:
        if '*' in my_list or '/' in my_list:
            if '*' in my_list and ('/' not in my_list or my_list.index('*') < my_list.index('/')):
                i = my_list.index('*')
                res = my_list[i-1] * my_list[i+1]
                my_list[i-1] = res
                my_list.pop(i+1)
                my_list.pop(i)
            else:
                i = my_list.index('/')
                res = my_list[i-1] / my_list[i+1]
                my_list[i-1] = res
                my_list.pop(i+1)
                my_list.pop(i)
        elif '+' in my_list or '-' in my_list:
            if '+' in my_list and ('-' not in my_list or my_list.index('+') < my_list.index('-')):   
                i = my_list.index('+')
                res = my_list[i-1] + my_list[i+1]
                my_list[i-1] = res
                my_list.pop(i+1)
                my_list.pop(i)
            else:
                i = my_list.index('-')
                res = my_list[i-1] - my_list[i+1]
                my_list[i-1] = res
                my_list.pop(i+1)
                my_list.pop(i)
    return res


# my_string = input('Введите арифметическое выражение: ')
s = '24/3-3+5*3/7+3+5'
my_list = calc(s)
print(calc(s))
print(eval(s))
print(decision(my_list))