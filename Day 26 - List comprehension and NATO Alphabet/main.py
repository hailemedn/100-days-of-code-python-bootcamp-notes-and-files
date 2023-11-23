# numbers = [1, 2, 3]
# # old way
# new_list1 = []
# for num in numbers:
#     new_num = num + 1
#     new_list1.append(new_num)
# print(new_list1)
#
# # with list comprehension
# new_list2 = [item + 1 for item in numbers]
# print(new_list2)
#
# # list comprehension also works for other sequences like a string
# name = "Angela"
# new_list3 = [letter for letter in name]
# print(new_list3)
#
# # python sequences
# # list, range, string, tuple
#
# # range as a list
# new_list4 = [item * 2 for item in range(1, 5)]
# print(new_list4)
#
# # conditional list comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# long_names_in_caps = [name.upper() for name in names if len(name) > 4]
# print(long_names_in_caps)

# keyword method
# list = ["item1", "item2", "item3"]
# new_list = [new_item for item in list if test]

# code challenge 26.1
# Instructions You are going to write a List Comprehension to create a new list called
# squared_numbers. This new list should contain every number in the list numbers but each number should be squared.
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# # Write your 1 line code 👇 below:
# squared_numbers = [num**2 for num in numbers]
#
#
# # Write your code 👆 above:
#
# print(squared_numbers)


# code challenge 26.2
# Instructions You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
# Example Output
# [2, 8, 34]
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# # Write your 1 line code 👇 below:
# result = [num for num in numbers if num % 2 == 0]
#
# # Write your code 👆 above:
#
# print(result)


# code challenge 26.3
# 💪 This exercise is HARD Instructions Take a look inside file1.txt and file2.txt. They each
# contain a bunch of numbers, each number on a new line. You are going to create a list called result which contains
# the numbers that are common in both files. e.g. if file1.txt contained: 1 2 3 and file2.txt contained: 2 3 4
# result = [2, 3]
# IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension
# instead of a Loop. Example Output [3, 6, 5, 33, 12, 7, 42, 13] Hint Use the keyword method for starting the List
# comprehension and fill in the relevant parts. First, you will need to read from the files and create a list using
# the lines in the files. This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp
# Remember you can check if a value exists in a list using the in keyword.
# https://www.w3schools.com/python/ref_keyword_in.asp
# Remember you can convert a string to an int using the int() method. https://www.w3schools.com/python/ref_func_int.asp

with open("file1.txt") as f1:
    file1_list = f1.readlines()
with open("file2.txt") as f2:
    file2_list = f2.readlines()

print(file1_list)
print(file2_list)
result = [int(item) for item in file1_list if item in file2_list]
# Write your code above 👆

print(result)

