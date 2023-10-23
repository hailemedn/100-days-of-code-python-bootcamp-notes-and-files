# def greet():
#     print("Hello")
#     print("World")
#     print("Again")

# greet()


# name = "Angela"
# name is parameter, Angela is the argument

# def greet_with_name(name):
#     print(f"Hello {name}")

# greet_with_name("Angela")


# functions with more than 1 input

# def greet_with(name, location):
#     print(f"{name} lives in {location}")

# # positional argument
# greet_with("haile", "summit")


# # keyword argument
# greet_with(location="Arabsa", name="haile")

import math
# code challenge
test_h = int(input("What is the height of the wall? "))
test_w = int(input("What is the width of the wall? "))
coverage = 5

def paint_calc(height, width, cover):
    cans = math.ceil((height * width) / cover)
    print(f"You need {cans} paint of cans.")


paint_calc(test_h, test_w, coverage)