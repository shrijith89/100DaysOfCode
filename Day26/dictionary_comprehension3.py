sentence = input("Enter the string").split(" ")
result = {word: len(word) for word in sentence}
print(result)
