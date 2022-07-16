# список (list()) - изменяемыйб, индексируемые my_list = [2, 3, 4, 5]
# кортеж (tuple())- неизменяемый, индексируемый my_tuple = (1, 2, 3, 4); my_tuple = ([my_list])
# множество (set()) - изменяемый, неиндексируемый, не содержит повторяющихся значений
# словарь (dict()) - изменяемый, ключ-значение,  

# my_set = set([1,2,2,12,2,1])
# my_set2 = {1,2,3,4,5,1,2,8, 3}
# my_set.add(4)
# my_set2.add(4)
# print(my_set2)

my_dict = {
    12: 'Стол',
    54: 'Кровать'
}
my_list = list(my_dict.values())
# print(my_dict)
print(my_list)

for key in my_dict.keys(): 
    print(key)

for val in my_dict.values():
    print(val)