
from twilio.rest import Client
import os
import requests
api_key = os.environ.get("OWM_API_KEY")
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC9d8664dd1476e9b7648b4d8ecfc43c2c"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 47.6062,
    "lon":-122.3321,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}
response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
first_twelve_hour_weather = weather_data["hourly"]
slice_above = first_twelve_hour_weather[:12] #got 0-11 hour
will_rain = False
for hour_data in slice_above:
    check_rain = hour_data["weather"][0]["id"]
    if check_rain < 700:
        will_rain = True

if will_rain:
    #print("bring the umbrella")       
    client = Client(account_sid, auth_token) 
    message = client.messages \
                .create(
                body="What do you call two straight days of rain in Seattle? - A weekend. ☔ ",
                from_='+12675507514',
                to='+14256244434'
                 )

print(message.status)
#http://jsonviewer.stack.hu/
#print(weather_data["hourly"][0]["weather"][0]["id"]) #804 id is printed
""" 
{}0
dt : 1640934000
temp : 271.91
feels_like : 271.91
pressure : 1008
humidity : 86
dew_point : 270.11
uvi : 0
clouds : 90
visibility : 6010
wind_speed : 0.49
wind_deg : 139
wind_gust : 0.58
[]weather #["weather]
{}0 #["weather][0]
id : 804
main : "Clouds"
description : "overcast clouds"
icon : "04n"
pop : 0.3
"""



    
