import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pick_cards(card_name):
    for i in range(2):
        card_name.append(random.choice(cards))
    return card_name


def calculate_sum(selected_cards):
    return sum(selected_cards)


user_cards = []
computer_cards = []
flag = 'y'


def initialize():
    pick_cards(user_cards)
    pick_cards(computer_cards)
    print("Computer selected {} ".format(computer_cards))
    print("Your cards {}, current score {}".format(user_cards, calculate_sum(user_cards)))


def decide_winner():
    if calculate_sum(user_cards) == 21:
        print("You Won.!")
    elif calculate_sum(computer_cards) == 21:
        print("You Lost! Computer Wins!")
    else:
        max_score()


def max_score():
    if calculate_sum(user_cards) > 21:
        if 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
            if calculate_sum(user_cards) > 21:
                print("You Lost, You went over!")
                exit()
            else:
                pick_new_card()
        else:
            print("You Lost, You went over.!")
            exit()
    else:
        pick_new_card()


def failed():
    print("Failure!")


def pick_new_card():
    global flag
    flag = input("Enter whether to continue the game or not. Enter 'y' or 'n' ")
    print("The current computer score is {}".format(calculate_sum(computer_cards)))

    if flag == 'y':
        user_cards.append(random.choice(cards))
        print("Your new card is {}".format(user_cards))
        decide_winner()
        max_score()
    else:
        failed()
    # max_score()


def play_game():
    print("Entered loop")
    if 11 in user_cards or 11 in computer_cards:
        decide_winner()
    else:
        print("Entered else part in play game")
        max_score()


initialize()
play_game()