# for loops
# fruits = ["Apple", "peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# range fun
# print 1 upto 9, steps by 2
# for num in range(1, 10, 2):
#     print(num)

# adds num 1 to 101
# total = 0
# for num in range(1, 101):
#     total += num
# print(total)

# code challenge
# Write a program that calculate the sum of all the even numbers from 1 to 100, including 1 and 100
total = 0
for num in range(2, 101, 2):
    total += num
print(total)