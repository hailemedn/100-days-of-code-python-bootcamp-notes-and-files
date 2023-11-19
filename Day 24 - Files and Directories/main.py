# Added Some improvements to the snake game


# with open("my_file.txt") as file:
#     # read the contents of the file
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:

    # don't write with the first parameter only because it will be opened in read only mode
    # inorder to write we have to add the mode.
    # mode = "w" overwrites, mode = "a" appends
    # if the my_file doesn't exist in write mode, it will create the file.
    # only works in mode = "w" mode, and the file doesn't exist.
    # file.write("\nNew text")

# with keyword closes the file when we finish using it
# important to close to free up resources
# file.close()

with open("my_file.txt") as file:
    highscore = file.read()

print(highscore)

# new_highscore = 8
# with open("my_file.txt", mode="w") as file:
#     file.write(str(new_highscore))


