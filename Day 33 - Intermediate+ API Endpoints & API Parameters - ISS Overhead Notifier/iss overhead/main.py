import requests
from datetime import datetime
import smtplib

MY_EMAIL = "hailemedn@gmail.com"
PASSWORD = "yngn jhdh ktjl ohws"
MY_LAT = 8.980603 # Your latitude
MY_LONG = 38.757759 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if (MY_LAT - 5) < iss_latitude < (MY_LAT + 5) and (MY_LONG - 5) < iss_longitude < (MY_LONG + 5):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="hailemedin@gmail.com",
            msg="Subject:ISS nearby\n\n"
                "Look up!"
        )



