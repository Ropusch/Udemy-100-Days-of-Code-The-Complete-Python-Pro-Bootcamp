from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client


load_dotenv()

# Twilio setuo
twilio_sid = os.getenv("TWILIO_SID")
twilio_token = os.getenv("TWILIO_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
my_number = os.getenv("MY_NUMBER")
demo_number = "+18777804236"


client = Client(twilio_sid, twilio_token)

# setup other APIs
STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Corporation"
TRESHOLD_PERCENT = 0.1
ARTICLE_COUNT = 1  # so message isnt to long for twilio!

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
day_before_y = (datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")


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
    "language": "en",
    "sortBy": "popularity"
}


def get_response(url: str, parameters: dict):
    r = requests.get(url=url, params=parameters)
    r.raise_for_status()
    return r.json()

def get_stock_dif():
    r_stock = get_response(STOCK_ENDPOINT, stock_parameters)

    try:
        yesterday_close_price = float(r_stock["Time Series (Daily)"][yesterday]["4. close"])
        day_before_y_close_price = float(r_stock["Time Series (Daily)"][day_before_y]["4. close"])
    except KeyError:
        return -1, 0.1  # API rate limit is 25 requests per day
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
    for artic in r_news["articles"][:ARTICLE_COUNT]:
        new = {
            "title": artic["title"]    #,
            # "brief": artic["description"]   #,
            # "url": artic["url"]
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

if stock_dif[1] >= TRESHOLD_PERCENT:
    news = get_news()
    message_text = f"{STOCK}: {sign_to_arrow(stock_dif[0])}{stock_dif[1]}%\n\n"
    for article in news:
        message_text += f"Headline: {article['title']}\n"
        # message_text += f"Brief: {article['brief']}\n"
        # message_text += f"{article['url']}\n\n"
    # print(message)

    #   sending SMS with Twilio

    message = client.messages.create(
        body=message_text,
        from_=twilio_number,
        to=my_number
    )
    print(message.status)




