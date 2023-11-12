import math


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
    if coffee_type == "latte":
        if resources['water'] < 200 or resources['milk'] < 150 or resources['coffee'] < 24:
            return "No resource found for latte"
    elif coffee_type == "cappuccino":
        if resources['water'] < 250 or resources['milk'] < 100 or resources['coffee'] < 24:
            return "No resource found for cappuccino"
    elif coffee_type == "espresso":
        if resources['water'] < 50 or resources['coffee'] < 18:
            return "No resource found for espresso"
    else:
        return "Not Available"


def print_report():
    print("The water present is {}ml, The milk present is {}ml and the coffee present is {}g".format(resources["water"],
                                                                                                     resources['milk'],
                                                                                                     resources[
                                                                                                         'coffee']))


def process_coins():
    quarters_coins = float(input("How many quarters you have.?"))
    dimes_coins = float(input("How many dimes you have.?"))
    nickels_coins = float(input("How many nickels you have"))
    penny_coins = float(input("How many pennies you have"))

    total_value = (quarters_coins * 0.25) + (dimes_coins * 0.10) + (nickels_coins * 0.05) + (penny_coins * 0.01)

    return round(total_value, 2)


command = "on"
total_amount = 0

while command != "off":
    coffee_selection = input("What would you like? espresso/latte/cappuccino")
    if coffee_selection == "report":
        print_report()
    elif check_resources(coffee_selection) != "Not Available":
        total_amount = process_coins()

    elif total_amount < MENU[coffee_selection]['cost']:
        print("Insufficient amount for the coffee you selected, the price for {} was {}, the amount you paid was {}".format(coffee_selection,
                    MENU[coffee_selection]['cost'], total_amount))
    else:
        print("Here is your change {}".format(total_amount - MENU[coffee_selection]['cost']))
        print("Enjoy your coffee")
