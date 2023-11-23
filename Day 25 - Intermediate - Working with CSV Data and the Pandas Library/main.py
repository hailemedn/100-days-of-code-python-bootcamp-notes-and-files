# with open("weather_data.csv") as file:
#     data = file.readlines()
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data["temp"]))
# print(type(data))

# change dataframe to dictionary
# data_to_dic = data.to_dict()
# print(data_to_dic)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# # accomplishes the same as the above code
# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns
# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# fahrenheit_value = (monday_temp * 9/5) + 32
# print(fahrenheit_value)

# create a dataframe from scratch
# data_dic = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(data_dic)
# print(new_data)
#
# new_data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231121.csv")

black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

# black_col = black_squirrels["Primary Fur Color"]
# gray_col = gray_squirrels["Primary Fur Color"]
# cinnamon_col = cinnamon_squirrels["Primary Fur Color"]
#
# no_of_black_squirrels = black_col.count()
# no_of_gray_squirrels = gray_col.count()
# no_of_cinnamon_squirrels = cinnamon_col.count()

# print(black["Primary Fur Color"])

data_dic = {
    "Primary Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_squirrels, gray_squirrels, cinnamon_squirrels]

}

print(data_dic)
new_data = pandas.DataFrame(data_dic)
print(new_data)
new_data.to_csv("squirrel_data.csv")
