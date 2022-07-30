# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


# def find_uniq(my_list: list) -> list:
#     new_list = []
#     for i in range(len(my_list)):
#         if my_list[i] in my_list[:i] or my_list[i] in my_list[i:]:
#             continue
#         else:
#             new_list.append(i)
#     return new_list


def find_uniq(list):
    outputList = []
    for i in range(len(list)):
        if i == 0:
            if not (list[i] in list[i + 1 :]):
                outputList.append(list[i])
        elif i == len(list) - 1:
            if not (list[i] in list[:i]):
                outputList.append(list[i])
        else:
            if not ((list[i] in list[:i]) or (list[i] in list[i + 1 :])):
                outputList.append(list[i])
    return outputList


my_list = [1, 7, 1, 2, 3, 1, 5, 1, 5, 3, 10, 1] 
print('Изначальный список:', my_list)
print('Итоговый список', find_uniq(my_list))


