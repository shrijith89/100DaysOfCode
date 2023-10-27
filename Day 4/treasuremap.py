line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
#A2
if position[0]=='A':
    map[int(position[1])-1][0] = 'X'
elif position[0] == 'B':
    map[int(position[1]) - 1][1] = 'X'
else:
    map[int(position[1]) - 1][2] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")


# A better solution
abc = ['a','b','c']
letter = position[0].lower()
letter_index = abc.index(letter)
number_index = int(position[1])-1
map[number_index][letter_index] = 'X'
print(f"{line1}\n{line2}\n{line3}")