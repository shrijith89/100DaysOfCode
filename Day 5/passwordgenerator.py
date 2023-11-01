import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter_count = int(input("How many letters would you like in your password?"))
symbol_count = int(input("How many symbols would you like in your password?"))
number_count = int(input("How many numbers would you like in your password?"))

password = []

password += random.choices(letters, k=letter_count)
password += random.choices(symbols, k=symbol_count)
password += random.choices(numbers, k=number_count)

random.shuffle(password)
password_string = ''.join(password)
print("Your password is : ".format(password_string))