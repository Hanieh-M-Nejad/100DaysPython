# Cipher Text
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to Cipher Text game.")
def encode(text, shift):
    encoded_text = ""
    for i in text:
        if i == " ":
            encoded_text += " "
        else:
            index = alphabet.index(i)
            index -= shift
            i = alphabet[index]
            encoded_text += i
        # space
    print(encoded_text)
def decode (text, shift):
    decoded_text = ""
    for i in text:
        if i == " ":
            decoded_text += " "
        else:
            index = alphabet.index(i)
            index += shift
            i = alphabet[index]
            decoded_text += i
    print(decoded_text)

cipher_on = True
while cipher_on:
    request = input('Type "encode" or "E" to encrypt, type "decode" or "D" to decrypt text:\n').lower()
    text = input("Type your text!:\n")
    shift = int(input("Type the shift number:\n"))
    if request == "encode" or request == "e":
        encode(text, shift)
    elif request == "decode" or request == "d":
        decode(text, shift)
    should_continue = input('Do you want to continue? Type "Y" for yes and "N" for no.\n').lower()
    if should_continue == "n":
        cipher_on = False

