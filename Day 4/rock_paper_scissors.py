import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# my Atempt
options = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")) 
computer_choice = random.randint(0, 2)

if (choice >= 3 or choice < 0):
    print("Invalid Choice, You Lose!")
else:   
    print(options[choice])
    print("Computer Chose:")
    print(options[computer_choice])

# if (choice == computer_choice):
#     print("Draw")
# elif (choice == 0 and computer_choice == 1):
#     print("You Lose")
# elif (choice == 0 and computer_choice == 2):
#     print("You win")
# elif (choice == 1 and computer_choice == 0):
#     print("You Win")
# elif (choice == 1 and computer_choice == 2):
#     print("You Lose")
# elif (choice == 2 and computer_choice == 0):
#     print("You Lose")
# elif (choice == 2 and computer_choice == 1):
#     print("You win")
# else:
#     print("Invalid Choice")


# Improved code

    if (choice == 0 and computer_choice == 2):
        print("You win!")
    elif (choice == 2 and computer_choice == 0):
        print("You Lose!")
    elif (choice < computer_choice):
        print("You Lose!")
    elif (choice > computer_choice):
        print("You Win!")
    elif ( choice == computer_choice):
        print("Draw")
