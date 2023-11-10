import random

EASY = 10
HARD = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
turns = ""

if difficulty_level == 'hard':
    print("You have {} attempts remaining to guess the number".format(HARD))
    turns = HARD
elif difficulty_level == 'easy':
    print("You have {} attempts remaining to guess the number".format(EASY))
    turns = EASY
else:
    print("Invalid Input!")

assigned_number = random.randint(1, 100)
guess_number = 0


def play_game():
    global guess_number
    global turns
    while guess_number != assigned_number:
        while turns > 0 and guess_number != assigned_number:
            guess_number = int(input("Guess a Number.! "))
            if guess_number > assigned_number:
                print("Too High!")
                turns -= 1
                print("You have {} attempts".format(turns))
            elif guess_number < assigned_number:
                print("Too Low!")
                turns -= 1
                print("You have {} attempts".format(turns))
            else:
                print("You Win!")

        else:
            print("You have run out of chances!")
            break


play_game()
