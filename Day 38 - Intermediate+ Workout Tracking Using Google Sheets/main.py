import requests
APP_ID = "6cbebd306cbebd30"
API_KEY = "a7b79ce2ea088b28ed5d2dd9c4e3d2dd	—"

GENDER = "M"
WEIGHT_KG = "55"
HEIGHT_CM = "167"
AGE = "26"



exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


