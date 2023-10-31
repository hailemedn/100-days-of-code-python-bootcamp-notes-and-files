from art import logo, vs
from game_data import data
import random
import os

os.system("cls")
def formatter(slot):
    return f"{slot['name']}, {slot['description']}, from {slot['country']}"

def compare(answer, slot_A, slot_B):
    if slot_A["follower_count"] > slot_B["follower_count"]:
        return answer == "a" 
    else:
        return answer == "b"
    
print(logo)
score = 0
game_should_continue = True

slot_B = random.choice(data)

while game_should_continue:
    slot_A = slot_B
    slot_B = random.choice(data)

    if slot_A == slot_B:
        slot_B = random.choice(data)



    print(f"Compare A: {formatter(slot=slot_A)}")
    print(vs)
    print(f"Compare B: {formatter(slot=slot_B)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    slot_A["follower_count"]



    
    correct_answer = compare(answer, slot_A, slot_B)
    if correct_answer:
        os.system("cls")
        score += 1
        print(logo)
        print(f"You are right, Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry You were wrong, Final Score: {score}")

