import requests
MY_LONG = 38.757759
MY_LAT = 8.980603

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# response = requests.get(url="http://api.open-notify.org/iss-now.json?callback=CALLBACK")
# print(response)

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)

sunrise = data["results"]["sunrise"]
print(sunrise)
print(sunrise.split("T")[1].split(":")[0])