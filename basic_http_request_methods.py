import requests
import os
from datetime import datetime

PIXELA_URL = "https://pixe.la/v1/users"
USERNAME = os.getenv("my_username")
TOKEN = os.getenv("my_token")
GRAPH_ID = "graph1"

user_params = {
    "token":    TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":  "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_URL, json=user_params)
# print(response.text)

graph_url = f"{PIXELA_URL}/{USERNAME}/graphs"

graph_params = {
    "id":   GRAPH_ID,
    "name": "Keeping track of learning Python",
    "unit": "h",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response_graph = requests.post(url=graph_url, json=graph_params, headers=headers)
# print(response_graph.text)

post_pixel_url = F"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": f"{today.strftime('%Y%m%d')}",
    "quantity": input("How many hours did you learn today?")
}

response_pixel = requests.post(url=post_pixel_url, json=pixel_params, headers=headers)
print(response_pixel.text)

update_url = f"{post_pixel_url}/{today}"

# pixel_update_params = {
#     "quantity": "2"
# }

# update_pixel_response = requests.put(url=update_url, json=pixel_update_params, headers=headers)
# print(update_pixel_response.text)

# delete_url = f"{update_url}"
# delete_response = requests.delete(url=delete_url, headers=headers)
# print(delete_response.text)
