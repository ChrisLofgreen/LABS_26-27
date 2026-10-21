



# Lab 4: Bonus


# Modified base program from lab 2 (made it slightly cleaner with a separete function ("get_info()") to merge data from the two sources into "data")


# 1.

# weather.json reads:
'''
[
  {
    "city": "Stockholm",
    "country": "Sweden",
    "temperature": 11.6,
    "temperature_unit": "\u00b0C",
    "windspeed": 21.2,
    "windspeed_unit": "km/h"
  }
]
'''

# 2.




from api_client import get_json
import json, os, time


weather_data = []


def get_city_info(city_name):
    for city in weather_data:
        if city["city"].lower() == city_name.lower() and ((time.time() - city["timestamp"]) / 60) < 10:
            return"test"

    city = get_json("https://geocoding-api.open-meteo.com/v1/search", params= {"name" : city_name, "count": 1})
    
    try:
        city_info = [city["results"][0]["name"], 
                     city["results"][0]["country"], 
                     (city["results"][0]["latitude"], city["results"][0]["longitude"])]
    except KeyError:
        city_info = []
    
    return city_info


def get_weather(coordinates):
    latitude, longitude = coordinates
    weather = get_json("https://api.open-meteo.com/v1/forecast", params= {"latitude" : latitude, "longitude": longitude, "current": ["temperature_2m", "wind_speed_10m"]})
    
    try:
        weather_info = [weather["current"]["temperature_2m"], 
                    weather["current_units"]["temperature_2m"], 
                    weather["current"]["wind_speed_10m"], 
                    weather["current_units"]["wind_speed_10m"]]
    except TypeError:
        weather_info = []
    
    return weather_info



def get_info(user_city):
    city_info = get_city_info(user_city)
    if len(city_info) > 0:
        weather = get_weather(city_info[2])
        if len(weather) > 0:
            return {"city": city_info[0], 
                    "country": city_info[1], 
                    "temperature": weather[0], 
                    "temperature_unit": weather[1], 
                    "windspeed": weather[2], 
                    "windspeed_unit": weather[3],
                    "timestamp": time.time()}
        else:
             return "Weather not availible"
    else:
        return "City not found"



def save_data():
    config_data = weather_data
    weather_file = 'weather.json'

    with open(weather_file, 'w') as config_file:
        json.dump(config_data, config_file, indent=2)

    return f"\nData successfully written to {weather_file}"





weather_query = get_info(str(input("type city to get the weather:\n")).strip())

weather_data.append(weather_query)

save_data()