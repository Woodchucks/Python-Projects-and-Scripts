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

account_sid = TWILLO_SID
auth_token = TWILLO_AUTH_TOKEN
client = Client(account_sid, auth_token)

for news in get_news():
    message = client.messages \
                    .create(
                         body=str(news),
                         from_="+12626983056",
                         to="+48 111 111 111"   
                     )
    print(message.Status)

