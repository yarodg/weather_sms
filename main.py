import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
# API Auth key for openweathermap
AUTH_KEY = ""

# Latitude and Longitude for your location
MY_LAT = 50.325218
MY_LON = 19.133600

# sid and auth token for twilio account
ACCOUNT_SID = ""
AUTH_TOKEN = ""

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": AUTH_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["hourly"][0]["weather"][0]["id"])

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's going to 🌧️ today. Remember to bring an ☂️",

        # Telephone number from twilio account
        from_='',

        # Your telephone number
        to=''
    )
    print(message.status)

