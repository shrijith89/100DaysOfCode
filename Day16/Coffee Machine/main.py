from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    choice = input("Enter the coffee type you need? cappuccino, latte, espresso")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(choice):
            money.process_coins()


