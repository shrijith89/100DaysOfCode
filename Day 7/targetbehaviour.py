import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
guess_letter = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")