import requests
from twilio.rest import Client
from config import OPENWEATHER_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECEIVER_NUM

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"


parameters = {
    "lat": 49.319981,
    "lon": 123.072411,
    "cnt": 4,
    "appid": OPENWEATHER_API_KEY
}

response = requests.get(OWN_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_id = hour_data["weather"][0]["id"]
    if int(condition_id) < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring an ☔️- It's gonna rain!",
        from_=TWILIO_PHONE_NUMBER,
        to=RECEIVER_NUM
    )

    print(message.sid)
