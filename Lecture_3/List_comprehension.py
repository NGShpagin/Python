# my_list = []

# for i in range(1, 101):
#     if (i%2==0):
#         my_list.append(i)

# print(my_list)

def f(x):
    return x**3


my_list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(my_list)
