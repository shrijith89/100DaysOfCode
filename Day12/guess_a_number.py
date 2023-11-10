import random

EASY = 10
HARD = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")


def chances(level):
    if difficulty_level == 'hard':
        return HARD
    elif difficulty_level == 'easy':
        return EASY


turns = chances(difficulty_level)
assigned_number = random.randint(1, 100)
guess_number = 0

while guess_number != assigned_number:
    if turns == 0:
        print("You have run out of chances")
        print("The number was {}".format(assigned_number))
        break
    print("You have {} chances remaining".format(turns))
    guess_number = int(input("Guess a Number.! "))
    if guess_number > assigned_number:
        print("Too High!")
        turns -= 1
    elif guess_number < assigned_number:
        print("Too Low!")
        turns -= 1
    else:
        print("You Win!")
        break
