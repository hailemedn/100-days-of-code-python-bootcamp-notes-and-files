# #gives error, bc len function accepts string
# print(len(345))


# #prints the first letter, called substrings
# print("Hello"[0])

# #concatinates to string, doesn't add
# print("123"+"345")

# #INTEGERS
# #adds two integers
# print(123 + 345)


# #underscore used to increase readability, its the same as 123,456,789 
# 123456789
# 123_456_789

# #FLOAT
# 3.12334

#Boolean
#only two values, True or False


#Errors

# #gives error bc we can't concatinate a string with an interger
# num_char = len(input("What is your name: "))
# print("Your name has " + num_char + " characters")

# #outputs the datatype of a variable
# print(type(num_char))

# #converts into a string 
# new_num_char = str(num_char)

# #this code works fine now 
# print("Your name has " + new_num_char + " characters")


# #converts to float
# a = float(123)




# #Challege 2.1
# #Take a two digit number input and adds them to each other
# two_digit_num = input("Input a two digit number: ")
# first_digit = two_digit_num[0]
# second_digit = two_digit_num[1] 

# result = int(first_digit) + int(second_digit)
# print(result) 



# #Some Aritmitic
# 3 + 5
# 7 - 4
# 3 * 4



# #division  outputs a float type
# divide = 8 / 2
# print(type(divide))


# #raise a number to a power/ exponent
# print(2 ** 3)   # outputs 8


#PEMDAS -  priority in execution - Left to right
# ()
# **        
# */    -    priorty LR  
# +-
# print(3 * (3 + 3) / 3 - 3)



# #chops of everything after the decimal, it doesn't round
# print(int(8/3))  # outputs 2

# #rounds it to 3
# print(round(8/3))  # outputs 3

# # rounds to 2 decimal places
# print(round(8/3,2))  # outputs 2.67


# # converts the type output into an integer, 
# # which means it removes everything after the decimal
# print(8//3)


# # uses the previous version, similar to result = result / 2
# result = 4 / 2
# result /= 2
# user = 0
# user += 1         # user adds 1 to it's previous value
# user -= 1
# user *= 1
# user /= 1



# score = 0
# height = 1.8
# isWinning = True 
# # f-String - allows us print different datatypes without converting 
# print(f"Your score is {score} and my height is {height} and everything we say is {isWinning}")
