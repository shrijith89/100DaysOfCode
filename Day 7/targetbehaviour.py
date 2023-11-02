import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
guess_letter = input("Guess a letter: ").lower()

for i in range(len(chosen_word)-1):
    if chosen_word[i] in guess_letter:
        print("Right")
    else:
        print("Wrong")