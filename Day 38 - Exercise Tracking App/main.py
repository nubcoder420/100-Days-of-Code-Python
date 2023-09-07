import requests
from datetime import datetime

APP_ID = "YOUR ID HERE"
API_KEY = "YOUR API KEY HERE"
SHEETY_TOKEN = "YOUR TOKEN HERE"

GENDER = "male"
WEIGHT_KG = 65.0
HEIGHT_CM = 165.0
AGE = 37

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
ADD_ROW_SHEETY_ENDPOINT = "YOUR SHEETY ENDPOINT HERE"

user_exercise = input("Tell me which exercise/s you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

request_body = {
    "query": user_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=request_body, headers=headers)
response.raise_for_status()

data = response.json()

current_datetime = datetime.now()
time = current_datetime.time()
date = current_datetime.date()
current_time = time.strftime("%H:%M")
current_date = date.strftime("%d/%m/%Y")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in data["exercises"]:
    sheety_parameters = {
          "workout": {
              "date": current_date,
              "time": current_time,
              "exercise": exercise["name"].title(),
              "duration": exercise["duration_min"],
              "calories": exercise["nf_calories"],
            }
        }

    sheet_response = requests.post(url=ADD_ROW_SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)

    # print(response.text)




