# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# we need a third variable to not lose the value of one of the variables
# if just assign b's value to a, then we won't have the a's original value, so that means we can't assign it to b later. 
# which means both variables will contain the same value. since we replaced a's value with b's value. 
c = a
a = b
b = c



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)