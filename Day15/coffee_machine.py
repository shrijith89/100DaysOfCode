MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 50,
}

unavailable_resource = ""


def check_resources(type_of_coffee):
    coffee = MENU[type_of_coffee]['ingredients']
    for coffee_ingredients in coffee:
        if resources[coffee_ingredients] < coffee[coffee_ingredients]:
            print("There is no enough {}".format(coffee_ingredients))
            return False
    return True


def print_report():
    print("The water present is {}ml, The milk present is {}ml and the coffee present is {}g"
          .format(resources["water"], resources['milk'], resources['coffee']))


def process_coins():
    total_value = 0
    total_value += float(input("How many quarters you have.? ")) * 0.25
    total_value += float(input("How many dimes you have.? ")) * 0.10
    total_value += float(input("How many nickels you have.? ")) * 0.05
    total_value += float(input("How many pennies you have.? ")) * 0.01
    return round(total_value, 2)


is_on = True
total_amount = 0


def make_coffee(coffee_typ):
    coffee = MENU[coffee_typ]['ingredients']
    for coffee_ingredients in coffee:
        resources[coffee_ingredients] -= coffee[coffee_ingredients]
    print("Coffee is ready, Enjoy the {}".format(coffee_typ))


def transaction_successful(coffee, amount):
    # Check for change and refund
    if amount == MENU[coffee]['cost']:
        return True
    elif amount > MENU[coffee]['cost']:
        print("Coffee is ready, the amount you paid was {}".format(amount))
        print("The change of amount {} is processed".format(round(amount - MENU[coffee]['cost'], 2)))
        return True
    else:
        print("Insufficient amount")
        return False


while is_on:
    user_input = input("What would you like? espresso/latte/cappuccino ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print_report()
    else:
        if check_resources(user_input):
            amount_received = process_coins()
            if transaction_successful(user_input, amount_received):
                make_coffee(user_input)
