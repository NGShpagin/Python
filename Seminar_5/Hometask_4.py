# Домашнее задание. Здаача 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# def input(data):
#     my_dict = {}
#     my_dict[data[0]] = 1
#     for i in range(1, len(data)):
#         if my_list[i] in my_dict.keys():
#             my_dict[data[i]] += 1
#         else:
#             my_dict[data[i]] = 1
#     return my_dict



def inRLE(my_string):
    result_string = '' 
    count = 1 
    for i in range(len(my_list)): 
        if i+1 < len(my_list) and my_list[i] == my_list[i+1]:                     
            count += 1 
        elif i+1 < len(my_list) and my_list[i] != my_list[i+1]: 
            result_string += f'{count}{my_list[i]}' 
            count = 1 
        else: 
            result_string += f'{count}{my_list[i]}' 
            count = 1 
    return result_string
        

def outRLE(result_string):
    new_string = ''
    for i in range(len(result_string)):
        if result_string[i].isdigit():
            num = int(result_string[i])
            while num !=0:
                new_string += f'{result_string[i+1]}'
                num -= 1
    return new_string


my_string = 'wwyeewqwqeq'
my_list = [i for i in my_string]
result_string = inRLE(my_string)
print(result_string)
print(outRLE(result_string))