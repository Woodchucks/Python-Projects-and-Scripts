import pandas as pd
import datetime as dt
from random import choice
import smtplib

EMAIL = "pettit.bear3@gmail.com"
PASSWORD = "P3ttit.b34r"

birthdays_dict = pd.read_csv("birthdays.csv").to_dict()
birthday_dataframe = pd.DataFrame.from_dict(birthdays_dict)
now = dt.datetime.now()
current_month = now.month
current_day = now.day
global file
global letter_file

# ----------------------Check if today matches a birthday-----------------------
def search_birthday_name():
    for _ in range(len(birthday_dataframe)-1):
        if birthday_dataframe["month"][_] == float(current_month) and birthday_dataframe["day"][_] == float(current_day):
            return birthday_dataframe["name"][_]

# --------------------Choose letter-------------------
def choose_letter():
    global file
    global letter_file
    letter_nr = choice(range(1,4))
    letter_file = f"letter_templates/letter_{letter_nr}.txt"
    file = open(letter_file, "r+")
    print("file created")

# ------------------change placeholder in letter to birthday name------
def replace_placeholder_name(name_placeholder, name):
    global file
    lines = file.readlines()
    for _ in lines:
        print(_)
        if name_placeholder in _:
            replacement = _.replace(name_placeholder, name)
            file.seek(0)
            file.writelines(replacement)
    file.close()

# ---------------------SEND EMAIL--------------------------------
def send_email():
    with open(letter_file) as f:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="pettit.bear@yahoo.com",
                msg=f"Subject:Happy Birthday!\n\n{f.read()}"
            )

# ---------------------MAIN---------------------------------------
name = search_birthday_name()
choose_letter()
replace_placeholder_name("[NAME]", name)
send_email()
