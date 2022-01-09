import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILLO_SID = os.environ.get("TWILLO_SID")
TWILLO_AUTH_TOKEN = os.environ.get("TWILLO_AUTH_TOKEN")
sign = ""
perc =""
formatted_article: dict

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":   STOCK,
    "interval": "60min",
    "slice":    "year1mont",
    "apikey":   STOCK_API_KEY,
}

today = datetime.now().date()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def print_get_news(news: dict):
    global sign
    stock_response = requests.get(url=STOCK_URL, params=stock_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()

    yesterday_close = stock_data["Time Series (Daily)"][yesterday]["4. close"]
    day_before_yesterday_close = stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"]

    perc = round(float(yesterday_close)*100/float(day_before_yesterday_close), 2) - 100

    if perc >= 105:
        sign = "▲"
        print(news)
    elif perc <= 95:
        sign = "▼"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    global formatted_article
    news_parameters = {
        "q": "Tesla",
        "from": yesterday,
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    top_3_title_list = [news_data["articles"][x]["title"] for x in range(0, 3)]
    top_3_news_body_list = [news_data["articles"][x]["description"] for x in range(0, 3)]

    top_3_news_dict = zip(top_3_title_list, top_3_news_body_list)
    print(top_3_news_dict)

    formatted_article = [f"{STOCK}: {sign}{perc}%\nHeadline: {key}\nBrief: {value}\n\n" for key, value in top_3_news_dict]
    return formatted_article

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = TWILLO_SID
auth_token = TWILLO_AUTH_TOKEN
client = Client(account_sid, auth_token)

for news in get_news():
    message = client.messages \
                    .create(
                         body=str(news),
                         from_="+12626983056",
#                        change number
                         to="+48 111 111 111"   
                     )
    print(message.Status)

#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

