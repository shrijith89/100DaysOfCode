alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet_list = list(text)


def caesar_cipher(direction_side, text, shift_amount):
    if direction_side == "encode":
        encrypted_message = ""
        for i in range(0, len(alphabet_list)):
            if alphabet_list[i] in alphabet:
                encrypted_message += alphabet[alphabet.index(alphabet_list[i]) + shift_amount]
        print("The encrypted message is {}".format(encrypted_message))
    elif direction_side == "decode":
        decrypted_message = ""
        for i in range(0, len(alphabet_list)):
            if alphabet_list[i] in alphabet:
                decrypted_message += alphabet[alphabet.index(alphabet_list[i]) - shift_amount]
        print("The decrypted message is {}".format(decrypted_message))
    else:
        print("Invalid direction!")


caesar_cipher(direction_side=direction, text=alphabet_list, shift_amount=shift)