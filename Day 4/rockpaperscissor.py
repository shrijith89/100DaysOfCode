import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("Type 0 for rock, Type 1 for paper and 2 for scissors"))
game_images = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

print("Computer chose: ")
print(game_images[computer_choice])
print("User chose: ")
print(game_images[user_choice])

if ((user_choice == 2 and computer_choice == 1) or \
        (user_choice == 1 and computer_choice == 0) or (user_choice == 0 and computer_choice == 2)):
    print("You Win")
elif user_choice == computer_choice:
    print("It's a draw")
elif user_choice >= 3 or user_choice < 0:
    print("Invalid number")
else:
    print("You lose!")