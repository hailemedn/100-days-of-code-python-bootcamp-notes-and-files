import requests
api_key = "6bf99c73664b55fefef2ee9497809109"

weather_params = {
    "lat": 8.980603,
    "lon": 38.757759,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=weather_params)
print(response.status_code)
