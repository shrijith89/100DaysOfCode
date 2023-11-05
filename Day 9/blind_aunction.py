import subprocess
import sys


def clear_screen():
    operating_system = sys.platform
    if operating_system == "win32":
        subprocess.run('cls', shell=True)


def bid_aunction():
    bidders = {}
    max_amount = 0
    name_of_the_bidder = ""
    flag = "yes"
    while flag == "yes":
        name = input("What is your name?: ")
        bid_amount = int(input("What is your bid? : $"))
        flag = input("Are there any other bidders? Type 'yes' or 'no'. ")
        bidders[name] = bid_amount
        if flag == "yes":
            clear_screen()
        else:
            for bidder_name in bidders:
                amount = bidders[bidder_name]
                if amount > max_amount:
                    max_amount = amount
                    name_of_the_bidder = bidder_name
            print("The maximum amount is {} and the winner is {}".format(max_amount, name_of_the_bidder))


bid_aunction()