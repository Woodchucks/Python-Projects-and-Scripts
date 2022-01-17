from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

city = []
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == '':
        row["iataCode"] = flight_search.get_iataCodes(row["city"])
        data_manager.update_iata_code(row["id"], row["iataCode"])
    flight_search.search_flight(row["iataCode"], row["lowestPrice"])
if flight_search.price != '':
    notification_manager.send_notificaion(flight_search)
