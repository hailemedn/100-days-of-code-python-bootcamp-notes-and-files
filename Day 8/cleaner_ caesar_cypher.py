import os
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(message, shift_amount, cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_postion = (position + shift_amount) % 26
            end_text += alphabet[new_postion]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

end_program = False

while not end_program:
    os.system("cls")
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
    ceasar(message=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Do you want to continue? y/n: ")
    if restart == "n":
        end_program = True
