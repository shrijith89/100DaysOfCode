import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*', '+']

print("Welcome to the PyPassword Generator!")
letter_count = int(input("How many letters would you like in your password?"))
symbol_count = int(input("How many symbols would you like in your password?"))
number_count = int(input("How many numbers would you like in your password?"))

password = ""

for i in range(letter_count):
    password += random.choice(letters)

for i in range(symbol_count):
    password += random.choice(symbols)

for i in range(number_count):
    password += random.choice(numbers)

final_string = ''.join(random.sample(password, len(password)))
print(final_string)