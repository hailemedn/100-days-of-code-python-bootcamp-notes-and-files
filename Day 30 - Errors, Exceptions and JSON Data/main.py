# something that might cause an exception
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" "value"}
#     print(a_dictionary["key"])

# Do this if there was an exception
# except FileNotFoundError
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")

# Do this if there were no exception
# else:
#     content = file.read()
#     print(content)

# Do this no matter what happens
# finally:
#     raise TypeError("This is an error i made up")


# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)

# code challenge 30.1
# fruits = ["Apple", "Pear", "Orange"]
#
#
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)

# code challenge 30.2
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)
