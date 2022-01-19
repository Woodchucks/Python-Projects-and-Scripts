import os
import requests

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]
TOKEN = os.environ["SHEETY_TOKEN"]
API_KEY = os.environ["SHEETY_API_KEY"]
APP_ID = os.environ["SHEETY_APP_ID"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": TOKEN
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        result = response.json()
        self.destination_data = result["lowestPrices"]
        return self.destination_data

    def update_iata_code(self, id, code):
        new_data = {
            "lowestPrice": {
                "iataCode": code
            }
        }
        response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{id}", json=new_data, headers=headers)
        print(response.text)

    def add_user(self, name, surname, email):
        new_data = {
          "user": {
            "firstName": name,
            "lastName": surname,
            "email": email
          }
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=new_data, headers=headers)

    def get_user(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        result = response.json()["users"]
        users = []
        for _ in range(0, len(result)):
          users.append(result[_]["email"])
        return users
