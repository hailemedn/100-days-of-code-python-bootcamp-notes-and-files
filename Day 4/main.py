# mersenne twister - pythons pseudo random number generator

import random



# import my_module
# # Module - separate code of functionality that are included to extend functionality
# print(my_module.pi)

# # generates random integer
# random_int = random.randint(1,10)
# print(random_int)

# # generates random float between 0 and 1
# random_float = random.random()
# print(random_float)


# # create a random decimal number between 0 and 5
# random_no = random.uniform(0, 5)
# print(random_no)


# # Heads or Tails Generator
# coin_flip = random.randint(0, 1)
# if (coin_flip == 1):
#     print("Heads")
# else:
#     print("Tails")



# Data Structure - a way or organizing and storing data
# List
# the first item is located at zero, because of offset, the first item is offset by 0, the second by 1, and on it goes.
# states_of_america = ["Delaware", "Pennsylvania"]
# print(states_of_america[0])

# we can also use - , -1 gets the last item
# print(states_of_america[-1])

# # Alter items in list
# states_of_america[1] = "Pencilvania"
# print(states_of_america[1])

# Add a single item in the list
# states_of_america.append("Angelaland")
# print(states_of_america)


# # add multiple items
# states_of_america.extend(["HaileLand, Ethiopia"])
# print(states_of_america)




# code challenge
# my Attempt
# names_input = input("Write everybody's name: ")

# # skips the comma and space and store the inputed strings in the list
# names = names_input.split(", ")
# payer = random.choice(names)
# print(f"{payer} is going to pay for the meal today.")


# # Angela Solution
# names_string = input("Give me everybody's name, separated by a comma: ")
# names = names_string.split(", ")
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# print(f"{person_who_will_pay} is going to pay for the meal.")


# when using the len function to access last item be sure to minus one for the offset

# Nested lists
fruit = ["apple", "banana", "peaches"]
vegetables = ["potato", "tomato", "Kale"]
combined = [fruit, vegetables]
print(combined)