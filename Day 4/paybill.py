import random

names_string = input("Enter the names")
names = names_string.split(", ")

print(names[random.randint(0, len(names)-1)])
