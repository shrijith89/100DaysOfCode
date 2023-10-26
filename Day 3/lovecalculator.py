print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

str3 = name1.lower() + name2.lower()

true_value = (str3.count('t') + str3.count('r') + str3.count('u') + str3.count('e'))
love_value = (str3.count('l') + str3.count('o') + str3.count('v') + str3.count('e'))

print(true_value)
print(love_value)

total_sum = int(str(true_value) + str(love_value))

if total_sum < 10 or total_sum > 90:
    print("Your score is {}, you go together like coke and mentos.".format(total_sum))
elif total_sum > 40 or total_sum < 50:
    print("Your score is {}, you are alright together.".format(total_sum))
else:
    print("Your score is {}".format(total_sum))