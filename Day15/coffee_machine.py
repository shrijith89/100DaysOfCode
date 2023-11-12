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


def check_resources(coffee_type):
    coffee = MENU[coffee_type]['ingredients']
    for coffee_ingredients in coffee:
        if resources[coffee_ingredients] < coffee[coffee_ingredients]:
            return False
    return True


def print_report():
    print("The water present is {}ml, The milk present is {}ml and the coffee present is {}g"
          .format(resources["water"], resources['milk'], resources['coffee']))


def process_coins():
    total_value = 0
    total_value += float(input("How many quarters you have.?")) * 0.25
    total_value += float(input("How many dimes you have.?")) * 0.10
    total_value += float(input("How many nickels you have")) * 0.05
    total_value += float(input("How many pennies you have")) * 0.01
    return round(total_value, 2)


is_on = True
total_amount = 0


def make_coffee(coffee_type):
    coffee = MENU[coffee_type]['ingredients']
    for coffee_ingredients in coffee:
        resources[coffee_ingredients] -= coffee[coffee_ingredients]


def transaction_successful():
    if check_resources(user_input):
        process_coins()
    else:



while is_on:
    user_input = input("What would you like? espresso/latte/cappuccino")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print_report()
    else:
        coffee_type = MENU[user_input]
        if check_resources():
            process_coins()
            print("Insufficient amount for the coffee you selected, the price for {} was {}, the amount you paid was {}"
                  .format(user_input, MENU[user_input]['cost'], total_amount))
        else:
            print("Here is your change {}".format(total_amount - MENU[user_input]['cost']))
            print("Enjoy your coffee")
