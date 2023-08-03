import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "03d467126321464d4ae9f8fde21ed351"

account_sid = "AC91dca104c290f1139ad5342d8b03b517"
auth_token = "7202a26ea0ffccbd3e52fbb2a077c368"

weather_params = {
    "lat": 20.705,
    "lon": 83.4863,
    "units":"metric",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
duration_list = weather_data["list"]

will_rain = False
for list in duration_list:
    condition_code = list["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Its going to rain today. Remember to bring an umbrella ☂️ ",
        to="whatsapp:+917327894942"
    )
    print(message.status)
# print(weather_data["list"][0]["weather"][0]["id"])




