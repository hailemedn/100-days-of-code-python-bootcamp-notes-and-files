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
import random

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

# with open("file1.txt") as f1:
#     file1_list = f1.readlines()
# with open("file2.txt") as f2:
#     file2_list = f2.readlines()
#
# print(file1_list)
# print(file2_list)
# result = [int(item) for item in file1_list if item in file2_list]
# Write your code above 👆

# print(result)

# simplified code in day 25 project using list comprehension.

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dic.items() if test}

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# students_score = {name: random.randint(1, 100) for name in names}
# print(students_score)
#
# passed_students = {student: score for (student, score) in students_score.items() if score > 50}
# print(passed_students)

# code challenge 26.4 - Dictionary comprehension
# Instructions You are going to use Dictionary Comprehension to create
# a dictionary called result that takes each word in the given sentence and calculates the number of letters in each
# word.

# Example Output
# {
# 'What': 4,
# 'is': 2,
# 'the': 3,
# 'Airspeed': 8,
# 'Velocity': 8,
# 'of': 2,
# 'an': 2,
# 'Unladen': 7,
# 'Swallow?': 8
# }
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# result = {words: len(words) for words in sentence.split()}
# print(result)

# code challenge 26.5
# Instructions You are going to use Dictionary Comprehension to create a dictionary called
# weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f
# Example Output
# {
# 'Monday': 53.6,
# 'Tuesday': 57.2,
# 'Wednesday': 59.0,
# 'Thursday': 57.2,
# 'Friday': 69.8,
# 'Saturday': 71.6,
# 'Sunday': 75.2
# }
#
# Hint
# Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.
#
# You can get each of the items from a dictionary using the .items() method:
# https://www.w3schools.com/python/ref_dictionary_items.asp
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
#
#
# print(weather_f)

# iterate over a dataframe
student_dict = {
    "student": ["Angela", "Haile", "Sokka"],
    "score": [16, 55, 78]
}

# looping through a dictionary
# for (key, value) in student_dict.items():
#     print(value)

# looping through a dataframe
import pandas
new_dataframe = pandas.DataFrame(student_dict)
# print(new_dataframe)
#
# for (key, value) in new_dataframe.items():
#     print(value)

# loop through rows of a dataframe
for (index, row) in new_dataframe.iterrows():
    # Access index and row
    # Access row.student or row.score
    print(row.student)


