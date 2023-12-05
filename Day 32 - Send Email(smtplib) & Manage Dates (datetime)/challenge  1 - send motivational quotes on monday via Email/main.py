import datetime as dt
import random
import smtplib

MY_EMAIL = "hailemedn@gmail.com"
PASSWORD = "yngn jhdh ktjl ohws"

# get the quotes from a file and put them in a list


# get the day tuesday
now = dt.datetime.now()
weekday = now.weekday()

# send a random quote if the day is tuesday
if now.weekday() == 1:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
    random_quote = random.choice(quotes_list)
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Tuesday Motivation\n\n"
                f"{random_quote}"
        )
