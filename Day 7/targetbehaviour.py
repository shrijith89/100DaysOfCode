import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
guess_letter = input("Guess a letter: ").lower()

display = []

for letter in range(len(chosen_word)):
    display += '_'

for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess_letter:
        display[letter] = guess_letter

print(display)