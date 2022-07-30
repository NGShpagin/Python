# Дан список чисел.
# Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.

#     *Пример:*
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


# def func(num):
#     my_list = []
#     my_list.append(a[num])
#     for i in range(num, len(a)):
#         if a[i] > my_list[-1]:
#             my_list.append(a[i])
#     numb = num
#     while numb != -1:
#         if a[numb] < my_list[0]:
#             my_list.insert(0, a[numb])
#         numb -= 1
#     print(my_list)


my_list = [1, 5, 2, 3, 4, 6, 1, 7]

# for i in range(len(a)):
#     func(i)


def max_in_list(my_list):
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max

my_dict = {}



def search(my_list):
    index = 0
    for n in range(1,len(my_list)):
        for i, item in enumerate(my_list[:-n]):
            new_list = [my_list[i]]
            for j, item_2 in enumerate(my_list[i+n:]):
                if item_2 > max_in_list(new_list):
                    new_list.append(item_2)
            if new_list not in my_dict.values():
                my_dict[index] = new_list
                index += 1
    return my_dict

for i in search(my_list):
    print(f"{i} : \t{my_dict[i]}")