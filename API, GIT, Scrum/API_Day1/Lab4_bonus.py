



# Lab 4: Bonus


# Modified base program from lab 2 (made it slightly cleaner with a separete function ("get_info()") to merge data from the two sources into "data")

from api_client import get_json
from retry_requests import retry


def get_city_info(city_name):
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
            return f"{city_info[0]}, {city_info[1]}: {weather[0]} {weather[1]}, wind {weather[2]} {weather[3]}"
        else:
             return "Weather not availible"
    else:
        return "City not found"


data = get_info(str(input("type city to get the weather:")).strip())

print(data)


# 1.