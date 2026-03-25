from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta


STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Corporation"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
day_before_y = (datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")

load_dotenv()
stock_api_key = os.getenv("STOCK_API_KEY_2")
news_api_key = os.getenv("NEWS_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
    "outputsize": "compact"
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api_key,
    "from": day_before_y,
    "language": "en"
}


def get_response(url: str, parameters: dict):
    r = requests.get(url=url, params=parameters)
    r.raise_for_status()
    return r.json()

def get_stock_dif():
    r_stock = get_response(STOCK_ENDPOINT, stock_parameters)

    yesterday_close_price = float(r_stock["Time Series (Daily)"][yesterday]["4. close"])
    day_before_y_close_price = float(r_stock["Time Series (Daily)"][day_before_y]["4. close"])
    if yesterday_close_price - day_before_y_close_price != 0:
        percent_dif = 100 * abs(yesterday_close_price - day_before_y_close_price) / yesterday_close_price
        up_down = (yesterday_close_price - day_before_y_close_price) / abs(yesterday_close_price - day_before_y_close_price)
    else:
        percent_dif = 0
        up_down = 0
    return up_down, round(percent_dif, 2)

def get_news():
    r_news = get_response(NEWS_ENDPOINT, news_parameters)
    headlines = []
    for artic in r_news["articles"][:3]:
        new = {
            "title": artic["title"],
            "brief": artic["description"],
            "url": artic["url"]
        }
        headlines.append(new)
    return headlines

def sign_to_arrow(sign: int):
    if sign == 1:
        return "🔺"
    elif sign == -1:
        return "🔻"
    else:
        return "❓"


stock_dif = get_stock_dif()

if stock_dif[1] >= 0.05:
    news = get_news()
    message = f"{STOCK}: {sign_to_arrow(stock_dif[0])}{stock_dif[1]}%\n\n"
    for article in news:
        message += f"Headline: {article['title']}\n"
        message += f"Brief: {article['brief']}\n"
        message += f"{article['url']}\n\n"
    print(message)




## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

