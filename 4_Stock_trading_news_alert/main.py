import requests
from twilio.rest import Client

TWILIO_SID = "AC91dca104c290f1139ad5342d8b03b517"
TWILIO_AUTH_TOKEN = "7202a26ea0ffccbd3e52fbb2a077c368"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY= "6111XR1XUSCGSGFO"
NEWS_API = "8f0cf78cbe3c4dada65c99f8d1711219"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


parameter1 = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT,params=parameter1)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
# print(yesterday_closing_price)

day_before_yesterday_closing_price = data_list[1]["4. close"]
# print(day_before_yesterday_closing_price)
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))



diff_percentage = round((difference / float(yesterday_closing_price))*100,2)
# print(diff_percentage)

if diff_percentage>1:
    new_params = {
        "apiKey":NEWS_API,
        "qInTitle":COMPANY_NAME
    }
    new_response = requests.get(NEWS_ENDPOINT,params=new_params)
    articles = new_response.json()["articles"]

    three_article = articles[:4]
    # print(three_article)

    round_diff = round(difference, 2)
    price = 0
    if float(yesterday_closing_price) > float(day_before_yesterday_closing_price):
        price=f"TSLA: {diff_percentage}% (${round_diff})🔺 "
    elif float(day_before_yesterday_closing_price) > float(yesterday_closing_price):
        price = f"TSLA: {diff_percentage}%(${round_diff}) 🔻 "
    else:
        price = f"TSLA: 0% 🔺 "
    formatted_article = [f"{price} \n Headline: {article['title']}. \n Brief: {article['description']}" for article in three_article]


    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_article:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=article,
            to="whatsapp:+917327894942"
        )
        print(message.status)



