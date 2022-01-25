import os
import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['EMAIL_PASSWORD']

URL = "https://www.amazon.com/ECCO-Goretex-Waterproof-Primaloft-Insulated/dp/B09MJTFJQ4/ref=sr_1_1?crid=SP2GNXJ7MMDT&th=1&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
    "Accept-Language": "pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"
}

response = requests.get(URL, headers=headers)
result = response.text

soup = BeautifulSoup(result, "html.parser")
pretty_soup = soup.prettify()

price = soup.find(name="span", class_="a-offscreen").getText()
price_float = price.split("$")[1]

if float(price_float) < 200.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="pettit.bear@yahoo.com",
            msg=f"Subject:Low Price Alert!\n"
                f"The item you were interested in reached your specified price range."
                f"Go ahead and purchase for ONLY ${price_float} under:\n{URL}"
        )
