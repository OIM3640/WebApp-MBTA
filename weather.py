import urllib.request
import json
from config import WEATHER_API_KEY
from mbta_helper import get_lat_long


def get_temp(place_name):
    APIKEY = WEATHER_API_KEY
    latitude, longtitude = get_lat_long(place_name)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longtitude}&appid={APIKEY}'
    print(url)

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        print(response_text)
        response_data = json.loads(response_text)
        weather =  response_data['main']['temp']
        weather = weather - 273.15
        return weather

def main():
    print(get_temp("Wellesley"))

if __name__ == "__main__":
    main()