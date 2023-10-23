alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import os

#part 4
#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

# part three
    #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar()
        # my attempt
def ceasar(message, shift_amount, cipher_direction):
    # plain_text = ""
    # cipher_text = ""
    # if cipher_direction == "encode":
    #     for letter in message:
    #         position = alphabet.index(letter)
    #         new_position = (position + shift_amount) % 26
    #         cipher_text += alphabet[new_position]
    #     print(f"The encoded text is {cipher_text}")
        
    # elif cipher_direction == "decode":
    #     for letter in message:
    #         position = alphabet.index(letter)
    #         new_position = (position - shift_amount) % 26
    #         plain_text += alphabet[new_position]
    #     print(f"The encoded text is {plain_text}")

    # part 4
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"


    # cleaner code
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

    #part 4
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).





    # part 1
    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
        #e.g. 
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        #print output: "The encoded text is mjqqt"

        ##HINT: How do you get the index of an item in a list:
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

        # my attempt
    # def encrypt(plain_text, shift_amount):
    #     cipher_text = ""
    #     for i in range(len(plain_text)):
    #         letter = plain_text[i]
    #         position = alphabet.index(letter)
    #         new_position = (position + shift_amount)%26
    #         cipher_text += alphabet[new_position]
    #     # print(''.join(message))
    #     print(f"The encoded text is: {cipher_text}")
    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    # encrypt(plain_text=text, shift_amount=shift)




    # part two
    #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"

    # cleaner approach
    # def decrypt(cipher_text, shift_amount):
    #     plain_text = ""
    #     for letter in cipher_text:
    #         position = alphabet.index(letter)
    #         new_position = (position - shift_amount) % 26
    #         plain_text += alphabet[new_position]
    #     print(f"The decoded text is {plain_text}")

    #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
    # if direction == "encode":
    #     encrypt(plain_text=text, shift_amount=shift)
    # elif direction == "decode":
    #     decrypt(cipher_text=text, shift_amount=shift)
    # else:
    #     print("Invalid direction.")




    
    ceasar(message=text, shift_amount=shift, cipher_direction=direction)
    continue_program = input("Do you want to continue? y/n: ")
    if continue_program == "n":
        end_program = True
