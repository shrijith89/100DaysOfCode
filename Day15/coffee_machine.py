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
    "coffee": 100,
}


def check_resources(coffee_type):
    if coffee_type == "latte":
        if resources['water'] < 200 or resources['milk'] < 150 or resources['coffee'] < 24:
            return "No resource found for latte"
    elif coffee_type == "cappuccino":
        if resources['water'] < 250 or resources['milk'] < 100 or resources['coffee'] < 24:
            return "No resource found for cappuccino"
    else:
        if resources['water'] < 50 or resources['coffee'] < 18:
            return "No resource found for espresso"


def print_report():
    pass


def process_coins():
    pass


def make_coffee():
    pass


coffee_type = input("What would you like? espresso/latte/cappuccino")
check_resources(coffee_type)