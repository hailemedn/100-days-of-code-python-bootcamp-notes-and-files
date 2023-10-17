
# # if statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else: 
#     print("Sorry, you have to go taller before you can ride.")


# comparision operators
# <
# >
# >=
# <=
# ==
# !=


# # Nested if / else
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $8")
#     else:
#         print("Please pay $12")
# else: 
#     print("Sorry, you have to go taller before you can ride.")


# multiple if
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("child's tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $8")
        bill = 8
    else:
        print("Adult tickets are $12")
        bill = 12
    wants_photo = input("Do you want a phot taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else: 
    print("Sorry, you have to go taller before you can ride.")