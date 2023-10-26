# Dictionary
# {key: value, anotherkey, anothervalue}

# programming_dictionary = {
#     "bug": "An error in a program from running unexpected thing",
#     "Function": "A piece of code that you can easily call over and over again"
# }

# retriving items from dictionary
# print(programming_dictionary["bug"])

# # adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something again and again"
# print(programming_dictionary)

# # create an empty dictionary
# empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
# print(programming_dictionary["bug"])
# programming_dictionary["bug"] = "A moth in your computer"
# print(programming_dictionary["bug"])


# loop through a dictionary
# prints keys
# for thing in programming_dictionary:
#     print(thing)

# #prints values
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# # code challenge score to grades.py


# # nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }


# nesting  list in a dictionary
# nesting dictionary in a dictionary
# nesting dictionary in a list
# travel_log = [
#      {
#          "Country": "France",
#          "cities_visited": ["Paris", "Lille", "Dijion"], 
#          "total_visits": 12
#     } ,
#      {
#          "Country": "Germany",
#          "cities_visited" : ["Berlin", "shalke, Bayern"], 
#          "total_visits": 7
#     },
# ]

# # list nested in a list valid
# ["a", "b", ["c,d"]]



# code challenge
travel_log = [
     {
         "Country": "France",
         "visits": 12,
         "cities": ["Paris", "Lille", "Dijion"], 
    } ,
     {
         "Country": "Germany",
         "visits": 5,
         "cities" : ["Berlin", "shalke, Bayern"],   
    },
]

#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

# my_attempt works
# def add_new_country(country_visited, times_visited, cities_visited):
#     global travel_log
#     travel_log += [{
#         "country": country_visited,
#         "visits": times_visited,
#         "cities": cities_visited
#     }]

# Angela's code
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
