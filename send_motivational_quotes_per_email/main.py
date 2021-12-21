import smtplib
import datetime as dt
import random as rd

MY_EMAIL = "pettit.bear3@gmail.com"
PASSWORD = "P3ttit.b34r"

with open("quotes.txt") as q:
    lines = rd.choice(q.readlines())
    now = dt.datetime.now()
    if now.weekday() == 1:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="pettit.bear@yahoo.com",
                msg=f"Subject:Motivational Quote for YA!\n\n{lines}"
            )
