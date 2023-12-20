import random

names = ['Alex', 'Beth', 'Dave']

dict1 = {name: random.randint(1, 99) for name in names}
filtered_dict = {name: value for name, value in dict1.items() if value >= 60}
print(dict1)
print(filtered_dict)
