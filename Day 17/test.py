# class names are written in PascalCase
# almost everything else is written in snake_case
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # value assigned to all objects
        self.followers = 0
        self.following = 0

    # method
    def follow(self, user):
        self.following += 1
        user.followers += 1


# user_1 = User()
# # assigning attributes to an object
# user_1.id = "001"
# user_1.username = "ramos"
#
# # creating new object
# user_2 = User()
# user_2.id = "002"
# user_2.username = "sergio"

# instead of doing it like the above, we can initialize the attributes each user must have
# and pass in the values as parameters
user_1 = User("001", "ramos")
user_2 = User("002", "Sergio")

# print(user_1.id)
# print(user_2.id)
# print(user_1.followers)
# print(user_2.followers)

# calling a method
user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)