



# Lab 2: Your own tool


from api_client import get_json
from retry_requests import retry

# 1.
'''
response = get_json("https://geocoding-api.open-meteo.com/v1/search", params= {"name" : "Stockholm", "count": 1})
print(response)
print(response["results"][0]["latitude"], response["results"][0]["longitude"])
'''

# 2.
'''
city = get_json("https://geocoding-api.open-meteo.com/v1/search", params= {"name" : "Stockholm", "count": 1})
coordinates = (city["results"][0]["latitude"], city["results"][0]["longitude"])

latitude, longitude = coordinates

weather = get_json("https://api.open-meteo.com/v1/forecast", params= {"latitude" : latitude, "longitude": longitude, "current": ["temperature_2m", "wind_speed_10m"]})
print(weather["current_units"])
print(weather["current"])
'''

# 3-4.
'''
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

user_input = str(input("type city to get the weather:")).strip()

city_info = get_city_info(user_input)

if len(city_info) > 0:
    weather = get_weather(city_info[2])
    if len(weather) > 0:
        print(f"{city_info[0]}, {city_info[1]}: {weather[0]} {weather[1]}, wind {weather[2]} {weather[3]}")
    else:
        print ("Weather not availible")
else:
    print ("City not found")
'''