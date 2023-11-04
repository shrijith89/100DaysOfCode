# Write your code below this line 👇
def prime_checker(number):
    count = 0
    if number > 1:
        for i in range(1, number):
            if number % i == 0:
                count += 1
    else:
        print("Not a prime number")

    if count == 1:
        print("A prime number")
    else:
        print("It's not a prime number")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)