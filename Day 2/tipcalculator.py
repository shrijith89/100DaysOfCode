print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = float(input("How many people to split the bill? "))
total_amount = ((tip_amount/100) * total_bill) + total_bill
print("Each person should pay: {:.2f}".format(total_amount/no_of_people))