# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def find_uniq(my_list):
    new_list = []
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list


my_list = [2, 5, 'as', 7, 67, 'as', 7, 5, 'me']
print(find_uniq(my_list))
