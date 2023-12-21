sentence = input("Enter the string")
result = {word: len(word) for word in sentence.split(" ")}
print(result)
