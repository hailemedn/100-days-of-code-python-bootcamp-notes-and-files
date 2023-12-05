##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
from datetime import datetime
import smtplib
import random

MY_EMAIL = "hailemedn@gmail.com"
PASSWORD = "yngn jhdh ktjl ohws"

# my_attempt
# data = pandas.read_csv("birthdays.csv")
#
#
# month_list = data.month.to_list()
# now = dt.datetime.now()
# current_month = now.month
# letter_list = ["letter_2.txt", "letter_1.txt", "letter_3.txt"]
# if current_month in month_list:
#     name = data[data.month == current_month].name.to_list()[0]
#     receiving_email = data[data.month == current_month].email.to_list()[0]
#     random_letter = random.choice(letter_list)
#     with open(f"letter_templates/{random_letter}") as file:
#         content = file.read()
#
#     new_letter = content.replace("[NAME]", name)
#     print(new_letter)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=receiving_email,
#             msg="Subject:Happy Birthday\n\n"
#                 f"{new_letter}"
#         )




# Angela's Solution
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
        print(content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday Angela's Solution\n\n"
                f"{content}"
        )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.




