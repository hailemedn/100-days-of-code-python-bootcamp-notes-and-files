from game_data import data
from art import logo, vs
import os
import random
os.system("cls")



# print(f"Compare A: 'name', 'description' , from 'country'")
# print(data[0]["name"])

# generate random account from the game data
def random_data_generator():
    return random.choice(data)

def compare(answer, data_A, data_B):
    if(answer == "a" and data_A["follower_count"] > data_B["follower_count"]):
        return True
    elif(answer == "b" and data_B["follower_count"] > data_A["follower_count"]):
        return True
    else:
        return False
    
def increament_score(score):
    return score + 1

data_A = random_data_generator()
data_B = random_data_generator()
score = 0

def game():
    print(logo)
    global data_A, data_B, score
    # format the account data into printable format
    print(f"Compare A: {data_A['name']}, {data_A['description']} , from {data_A['country']}")
    print(vs)
    print(f"Compare B: {data_B['name']}, {data_B['description']} , from {data_B['country']}")
    answer = input("who has more followers? 'A' or 'B': ").lower()
    print(data_A["follower_count"])
    print(data_B["follower_count"])

    correct_choice = compare(answer, data_A, data_B)
    if correct_choice:
        score += 1
        os.system("cls")
        print(f"You are right, current score: {score}")
        data_A = data_B
        data_B = random_data_generator()
        game()
    else:
        print(f"Sorry that's wrong, Final score: {score}")

game()
 
# data_A = data_B
# data_B = random_data_generator()
# print(f"Compare A: {data_A['name']}, {data_A['description']} , from {data_A['country']}")
# print(vs)
# print(f"Compare B: {data_B['name']}, {data_B['description']} , from {data_B['country']}")