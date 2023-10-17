# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# # my attempt - works perfect
# combined_name = name1 + name2
# combined_name = combined_name.lower()
# first_digit = combined_name.count("t")
# first_digit += combined_name.count("r")
# first_digit += combined_name.count("u")
# first_digit += combined_name.count("e")


# second_digit = combined_name.count("l")
# second_digit += combined_name.count("o")
# second_digit += combined_name.count("v")
# second_digit += combined_name.count("e")

# love_score = str(first_digit) + str(second_digit)
# love_score = int(love_score)

# if (love_score < 10) and (love_score > 90):
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score > 40) and (love_score < 50):
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")





# Angela solution
combined_name = name1 + name2
lowered_combined_name = combined_name.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) and (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")