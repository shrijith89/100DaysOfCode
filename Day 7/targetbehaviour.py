import random

word_list = ["ardvark", "baboon", "camel", "lion", "tiger", "elephant"]
chosen_word = random.choice(word_list)
display = []
lives = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

len_stages = len(stages) - 1

for letter in range(len(chosen_word)):
    display += '_'

while '_' in display:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter not in chosen_word:
        print("You guessed {}, that's not in the word. You lose a life".format(guess_letter))
        lives -= 1
        print(stages[len_stages])
        len_stages -= 1
        if lives < 0:
            print("You run out of chances, You Lost!")
            break
    elif guess_letter in display:
        print("You have already guessed the letter, Guess other letter")
    else:
        print("Guess is right!")
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guess_letter:
                display[letter] = guess_letter
    print(display)
else:
    print("You win!")