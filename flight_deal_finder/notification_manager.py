from twilio.rest import Client

TWILLO_SID = os.environ.get("TWILLO_SID")
TWILLO_AUTH_TOKEN = os.environ.get("TWILLO_AUTH_TOKEN")

class NotificationManager:

    def send_notificaion(self, flight_details):

        client = Client(TWILLO_SID, TWILLO_AUTH_TOKEN)

        message = client.messages \
            .create(
            body=f"Low price alert! Only {flight_details.price} PLN"
                 f"to fly from {flight_details.departure_city_name}-{flight_details.departure_airport_iata_code} "
                 f"to {flight_details.arrival_city_name}-{flight_details.arrival_airport_iata_code}, "
                 f"from {flight_details.from_date} to {flight_details.to_date}.",
            from_='+12626983056',
            to='#my phone nr
        )

        print(message.sid)
