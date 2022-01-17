import requests

SHEETY_PRICES_ENDPOINT = #my google sheet url
TOKEN = os.getenv("TOKEN")
API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")

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
