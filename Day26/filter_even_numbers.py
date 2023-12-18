string = "9, 0, 32, 8, 2, 8, 64, 29, 42, 99"
list_of_strings = string.split(",")

new_list = [int(n) for n in list_of_strings if int(n)%2==0]
print(new_list)
