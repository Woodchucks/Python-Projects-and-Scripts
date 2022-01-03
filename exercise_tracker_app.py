import requests
from datetime import datetime
import os

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")
NATURAL_LANGUAGE_URL = os.getenv("NATURAL_LANGUAGE_URL")
SHEETY_URL = os.getenv("SHEET_ENDPOINT")
TOKEN = os.getenv("TOKEN")

exercise_text = input("Enter your workout: ")

parameters = {
    "query": exercise_text,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": TOKEN
}

response = requests.post(url=NATURAL_LANGUAGE_URL, json=parameters, headers=headers)

result = response.json()

time = datetime.now().strftime("%X")
today = datetime.now().strftime("%d/%m/%Y")

for exercise in result["exercises"]:
    sheet_inputs = {
        "totalWorkout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheet_response = requests.post(url=SHEETY_URL, json=sheet_inputs, headers=headers)
print(sheet_response.text)
