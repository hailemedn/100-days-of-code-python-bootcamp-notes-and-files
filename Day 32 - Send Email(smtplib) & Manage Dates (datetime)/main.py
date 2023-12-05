# import smtplib
# my_email = "hailemedn@gmail.com"
# password = "yngn jhdh ktjl ohws"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="hailemedin@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


import datetime as dt

now = dt.datetime.now()
# print(now)
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1999, month=2, day=23, hour=4)
print(date_of_birth)
