from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# print("Welcome to Sandra's Flight Club")
# print("We find the best flight deals and email you")
# username = input("What is your first name?\n")
# surname = input("What is your last name?\n")
# email = input("What is your email?\n")
# email_verification = input("Type your email again\n")
# if email == email_verification:
#   print("You're in the club!\n")

city = []
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()
flight_search = FlightSearch()

# data_manager.add_user(username, surname, email)

# print(data_manager.get_user())

for row in sheet_data:
    if row["iataCode"] == '':
        row["iataCode"] = flight_search.get_iataCodes(row["city"])
        data_manager.update_iata_code(row["id"], row["iataCode"])
    flight_search.search_flight(row["iataCode"], row["lowestPrice"])
if flight_search.price != '':
    notification_manager.send_email(flight_search, data_manager)
