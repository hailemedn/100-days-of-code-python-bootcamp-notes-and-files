# scope
# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside {enemies}")


# increase_enemies() # 2
# print(f"enemies outside function {enemies}") # 1

# Global scope - not within any function
# global variable
# player_health = 10

# local scope - exists within function
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(potion_strength)
#         print(player_health)

# gives error because it has a local scope within it's parent      
# drink_potion()

# gives error because it's a local variable
# print(postion_strength)


# There is no block scope in python

# game_level = 3
# enemies  = ["skeleton", "Zombie", "Alien"]

# if game_level < 5
#     new_enemy = enemies[0]

# # valid
# print(new_enemy)


# game_level = 3
# def create_enemy():
#     enemies  = ["skeleton", "Zombie", "Alien"]

#     if game_level < 5
#         new_enemy = enemies[0]

# Invalid
# print(new_enemy)

# if you create a variable within a function, 
# then it's only available within the function

# but if you create a variable within a block of code
# such as if statement, while loops and similar blocks which have indentations, 
# the variable is still a global variable


# modifying global scopoe
# enemies = 1
# def increase_enemies():
    # creating a new variable that has a local scope
    # bad idea to name local and global variable with the same name
    # enemies = 2

    # now we are accessing the global variable
    # not recommended, because it can get confusing
    # avoid modifying global scope inside a function. 
    # global enemies
    # enemies += 1
    # print(f"enemies inside {enemies}")

    # the recommended way is to use return an output without modifying the global variable
    # return enemies + 1

# it now adds one to the current value of enemies everytime it's called but doesn't modify enemies.
# increase_enemies() # 2
# print(f"enemies outside function {enemies}") # 1 
# print(increase_enemies()) # 2


# Global Constants
# The naming convention is to make the name all caps, 
# so that when you see the name you will remember not to modify it
# PI = 3.14159
# URL = "google.com"
# TWITTER_HANDLE = "@haile"


