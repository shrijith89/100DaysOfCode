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
num2 = int(input("What is the second number.? "))
answer = 0
updated_answer = 0

flag = "y"
count = 0

while flag == "y":
    if count == 0:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation type from the above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print("{} {} {} = {}".format(num1, operation_symbol, num2, answer))

    flag = input("Do you want to continue.? Type 'y' for yes and 'n' for no ")
    if flag == "n":
        break
    else:
        updated_answer = answer
        num3 = int(input("Enter the third number "))
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation type from the above: ")
        count += 1
        calculation_function = operations[operation_symbol]
        answer = calculation_function(answer, num3)
        print("{} {} {} = {}".format(updated_answer, operation_symbol, num3, answer))