import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_sum(cards):
    sumofcards = 0
    for i in cards:
        sumofcards += i
    return sumofcards


def assign_cards(cardcollection):
    cardcollection = []
    for i in range(2):
        cardcollection.append(deal_card())
    return cardcollection


user_cards = assign_cards(deal_card())
computer_cards = assign_cards(deal_card())
need_card = False

def winner():
    updated_sum = 0
    if calculate_sum(user_cards) == 21:
        print("User Won.!")
    elif calculate_sum(computer_cards) == 21:
        print("User Lost! Computer Wins!")
    else:
        need_card = input("Do you want to select any other card, Type 'y' or 'n' ")
        if need_card == 'y':
            user_cards.append(assign_cards((deal_card())))
            for i in range(len(user_cards)):
                if user_cards[i] == 11:
                    user_cards[i] = 1
                updated_sum += user_cards[i]
winner()


def printfunc():
    print("The user cards ", user_cards)
    print("The computer cards ", computer_cards)
    print("The sum of cards of a user ", calculate_sum(user_cards))
    print("The sum of cards of a computer ", calculate_sum(computer_cards))


printfunc()
