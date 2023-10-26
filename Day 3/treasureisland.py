print("Welcome to Treasure Island. Your mission is to find the treasure")
direction = input("You're at cross road. Where do you want to go? Type 'left' or 'right'")
if direction == 'left':
    wait_or_swim = input("You've come to a lake. There is a island in the middle of the lake. Type 'wait' to wait for "
                         "a boat. Type 'swim' to swim across")
    if wait_or_swim == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, "
                      "and one blue. Which color do you chose?")
        if color == "red":
            print("Burned by fire. Game Over.")
        elif color == "blue":
            print("Eaten by beasts. Game over")
        elif color == "yellow":
            print("You win!")
        else:
            print("Game Over.")
    elif wait_or_swim == "swim":
        print("You get attacked by a angry trout. Game Over.")
    else:
        print("Game Over")

else:
    print("You fell into a hole. Game Over")

