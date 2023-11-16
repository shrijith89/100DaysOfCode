from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
moneyMachine = MoneyMachine()

order = input("Enter the coffee type you need? cappuccino, latte, espresso")
menu.find_drink(order)
moneyMachine.process_coins()
moneyMachine.make_payment(menu.cost)
