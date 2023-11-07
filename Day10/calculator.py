def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input("What is the first number.? "))
for i in operations:
    print(i)

flag = "y"
count = 0

while flag == "y":
    operation_symbol = input("Pick an operation : ")
    num2 = int(input("What is the next number.? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print("{} {} {} = {}".format(num1, operation_symbol, num2, answer))

    flag = input("Do you want to continue.? Type 'y' for yes and 'n' for no ")
    if flag == "n":
        flag = 'n'
    else:
        num1 = answer
