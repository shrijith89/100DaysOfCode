import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []

for letter in range(len(chosen_word)):
    display += '_'

while '_' in display:
    guess_letter = input("Guess a letter: ").lower()
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess_letter:
            display[letter] = guess_letter
    print(display)