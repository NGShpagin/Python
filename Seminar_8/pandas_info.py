import pandas as pd

d = {
    'Name': ['Petr', 'Sergey', 'Alex'],
    'Surname': ['Ivanov', 'Petrov', 'Sidorov'],
    'Birth year': [2011, 2012, 2013],
    'Class'
    'Place': [[1,2,2], [1,1,1], [2,1,1]],
    'Status': [5, 4, 3]}

df = pd.DataFrame(d)
print(df)

# path = ''
# df = pd.read_csv(path)