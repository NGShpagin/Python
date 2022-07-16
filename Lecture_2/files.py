# # Способ записи в файл 1
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors) #разделителей не будет
# data.write('\nLine2\n') 
# data.write('Line3\n') 
# data.close()

# exit()

# Способ записи в файл 2
# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()