import os
from art import logo


os.system("cls")
bidders = {}

def add_bidders(name, bid):
    bidders[name] = int(bid)
def find_highest_bidder(bidding_record):

    highest_bidder = max(bidding_record, key=bidding_record.get)
    print(f"The highest bidder is {highest_bidder}, with a bid of {bidding_record[highest_bidder]}")

    # Alternative way
    # highest_bid = 0
    # highest_bidder = ""
    # for key in bidding_record:
    #     if bidding_record[key] > highest_bid:
    #         highest_bid = bidding_record[key]
    #         highest_bidder = key
    # print(f"The highest bidder is {highest_bidder}, with a bid of {bidding_record[highest_bidder]}")

print(logo)
print("Welcome to the secret auction program")

end_of_bidding = False
while not end_of_bidding:
    bidder_name = input("What is your name?\n")
    bidder_bid = input("What is your bid\n")
    add_bidders(name=bidder_name, bid=bidder_bid)
    restart = input("are there more bidders? y/n\n").lower()
    if restart == "n":
        end_of_bidding = True
        find_highest_bidder(bidders)
    else:
        os.system("cls")



