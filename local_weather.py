import urllib.request
import json
from config import APIKEY_Weather

city = 'wellesley'
country_code = 'us'

def get_weather_conditions(city, country_code, APIKEY_Weather):
   
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY_Weather}'
    
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    weather_conditions = response_data['weather'][0]['description']
    
    return weather_conditions



def get_local_temperature(city, country_code, APIKEY_Weather):
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=imperial&appid={APIKEY_Weather}'

    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    temperature = response_data['main']['temp']

    return temperature




get_local_temperature(city,country_code,APIKEY_Weather)
get_weather_conditions(city, country_code, APIKEY_Weather)


def recommend_clothes(city, country_code, APIKEY_Weather):
    temperature = get_local_temperature(city, country_code, APIKEY_Weather)
    weather_conditions = get_weather_conditions(city, country_code, APIKEY_Weather)
    
    if temperature < 40:
        print("Remember to bring a jacket!")
    elif temperature > 75:
        print("It's time to wear lighter clothes!")
    if "rain" in weather_conditions.lower():
        print("Remember to bring an umbrella!")
    elif "snow" in weather_conditions.lower():
        print("Recommend staying inside.")
    if "clear" in weather_conditions.lower() or "sunny" in weather_conditions.lower():
        print("Remember sunglasses or a hat!")


recommend_clothes(city, country_code, APIKEY_Weather)
