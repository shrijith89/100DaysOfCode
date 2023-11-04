alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet_list = list(text)


def encode(direction=direction, text=text, shift=shift):
    encrypted_message = ""
    for i in range(0, len(alphabet_list)):
        if alphabet_list[i] in alphabet:
            encrypted_message += alphabet[alphabet.index(alphabet_list[i]) + shift]
    print("The encrypted message is {}".format(encrypted_message))


def decode(direction=direction, text=text, shift=shift):
    decrypted_message = ""
    for i in range(0, len(alphabet_list)):
        if alphabet_list[i] in alphabet:
            decrypted_message += alphabet[alphabet.index(alphabet_list[i]) - shift]
    print("The decrypted message is {}".format(decrypted_message))


if direction == "encode":
    encode(direction, text, shift)
elif direction == "decode":
    decode(direction, text, shift)
else:
    print("Invalid direction!")