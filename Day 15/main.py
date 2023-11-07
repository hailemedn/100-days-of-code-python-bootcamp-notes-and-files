from menu import MENU, resources
import os
os.system("cls")


def display_report():
    """prints out the remaining resources."""
    print("Remaining Resources")
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water : {water}ml")
    print(f"milk : {milk}ml")
    print(f"coffee : {coffee}g")
    print(f"money : ${money}")


def process_coins(quarter_coins, dime_coins, nickel_coins, penny_coins):
    """takes the coins, converts them into dollars and returns the total coins in dollars"""
    quarters_in_dollars = 0.25 * quarter_coins
    dimes_in_dollars = 0.1 * dime_coins
    nickels_in_dollars = 0.05 * nickel_coins
    penny_in_dollars = 0.01 * penny_coins
    total = quarters_in_dollars + dimes_in_dollars + nickels_in_dollars + penny_in_dollars
    return total


def make_coffee(coffee_ingredients, cost, coffee_choice):
    """takes coffee ingredients, price and your choice
    then decrease the amount of ingredients needed from resources
    and returns your coffee choice"""
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    resources["money"] += cost
    return print(f"Here's your {coffee_choice} 🍵, Enjoy")


def resource_checker(coffee_ingredients):
    """takes the ingredients needed to make the coffee
    and checks if there is enough resources to make the coffee"""
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        else:
            return True


resources["money"] = 0
continue_order = True


while continue_order:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == "report":
        display_report()
        continue
    elif answer == "off":
        break
    elif answer in MENU:
        data = MENU[answer]
        price = data["cost"]
        ingredients = data["ingredients"]
    else:
        print("Invalid Input")
        continue
    sufficient_resource = resource_checker(ingredients)

    if sufficient_resource:
        print("Please Enter coins")
        quarters = int(input("How many quarters: ")) 
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies: "))

        total_payment_in_dollars = process_coins(quarters, dimes, nickels, pennies)

        if total_payment_in_dollars > price:
            change = round(total_payment_in_dollars - price, 2) 
            print(f"Here's your change: {change}")
            make_coffee(ingredients, price, answer)
            
        elif total_payment_in_dollars == price:
            make_coffee(ingredients, price, answer)
            
        else:
            print("not enough coins, money refunded.")

