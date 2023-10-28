# easy has 10 attempts
# hard has 5 attempts
# when the user inputs a number, it tells them "too high" or "too low"
import random
import os
from art import logo
os.system("cls")

def guess_checker():
    '''checks whether the guess is correct or not'''
    global game_over
    global attempt
    if guess == random_number:
        print("Congradulations You guessed right, You win")
        game_over = True
    elif guess > random_number:
        attempt -= 1
        print("Too high")
    else:
        attempt -= 1
        print("Too low")


    if attempt == 0:
        game_over = True
        print("You are out of attempts, Game over")


print(logo)
random_number = random.randint(1, 100)
print(random_number)
level = input("Do you want 'easy' or 'difficult' level: ")
if level == "easy":
    attempt = 10
else:
    attempt = 5

game_over = False
while not game_over:
    print(f"attempts remaining: {attempt}")
    guess = int(input("Guess a number: "))
    guess_checker()
    
    



