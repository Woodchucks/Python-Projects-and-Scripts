import os
import requests
from twilio.rest import Client

TWILLO_SID = os.environ["TWILLO_SID"]
TWILLO_AUTH_TOKEN = os.environ["TWILLO_AUTH_TOKEN"]
USER_PHONE = os.environ["USER_PHONE"]
MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
text_message = ""

class NotificationManager:

    def send_notificaion(self, flight_details):
        global text_message
        client = Client(TWILLO_SID, TWILLO_AUTH_TOKEN)

        text_message = f"Low price alert! Only {flight_details.price} PLN to fly from {flight_details.departure_city_name}-{flight_details.departure_airport_iata_code} to {flight_details.arrival_city_name}-{flight_details.arrival_airport_iata_code}, from {flight_details.from_date} to {flight_details.to_date}.",

        message = client.messages \
            .create(
            body=text_message,
            from_='+12626983056',
            to=USER_PHONE
        )

        print(message.sid)

    def send_email(self, flight_details, user_details):
        users = user_details.get_user()
        for email in users:
          self.send_notificaion(flight_details)
          global text_message
          with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
              from_addr=MY_EMAIL,
              to_addrs=email,
              msg=(f"Subject:Cheap Flight Deals For You!\n\n{text_message}").encode('utf-8')
            )
