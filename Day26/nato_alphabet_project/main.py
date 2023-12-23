import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
dictionary = {row['letter']: row['code'] for index, row in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
value = input("Enter the string")
letters = [letter.upper() for letter in value]
result = [dictionary.get(letter) for letter in letters]
print(result)
