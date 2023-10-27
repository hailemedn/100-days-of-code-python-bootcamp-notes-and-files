############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import os
from art import logo
os.system("cls")

def deal_cards(card_list, amount):
    for i in range(amount):
        random_card = random.choice(cards)
        if random_card == 11 and sum(card_list) > 21:
            random_card == 1
        card_list.append(random_card)

def compare_cards(player, computer):
    total_player_score = sum(player)
    total_computer_score = sum(computer)
    if total_player_score > total_computer_score or total_computer_score > 21:
        print("You win")
    elif total_player_score == total_computer_score:
        print("Draw")
    else:
        print("You Lose")


def get_another_card():
    global player_cards, computer_cards
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if another_card == "n":
        while sum(computer_cards) < 17:
            print("computer score is lower than 17.\nAnother card for computer. ")
            deal_cards(computer_cards, 1)
            print(computer_cards)
        print(f"Your final hand {player_cards}")
        print(f"Computer's final hand {computer_cards}")
        compare_cards(player_cards, computer_cards)
        
        # we check if computer total score is less than 17, if that is so we append cards until it's over 17
    elif another_card == "y":
        deal_cards(player_cards, 1)
        total_player_score = sum(player_cards)
        if total_player_score > 21:
            print(f"Your final hand {player_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("Player Score is more than 21, You Lose")
        elif total_player_score == 21:
            print(f"Your final hand {player_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("black Jack, You win")
        else:
            print(f"Your current hand {player_cards}")
            get_another_card()
    

print(logo)
print("Welcome to blackJack!")
player_cards = []
computer_cards = []

deal_cards(player_cards, 2)
deal_cards(computer_cards, 2)

print(f"Your cards: {player_cards}")
print(f"Computer's first card: {computer_cards[0]}")

if sum(player_cards) == 21:
    print("Black Jack, You Win")
else:
    get_another_card()
    
            
            
        