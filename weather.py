# Getting Weather
import urllib.request
import json
import pprint
from mbta_helper import get_nearest_station

OPENWEATHERMAP_APIKEY = 'bd934d1c567130b31d6bebfff8abab04'


def weather(city: str) -> float:
    """ 
    This function gets the weather of the inputed city
    """
    city = city.replace(' ', '%20')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={OPENWEATHERMAP_APIKEY}&units=metric'
    # print(url)

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    return response_data['main']['temp']

# test it out


def main():
    """Testing out code"""
    print(weather())


if __name__ == '__main__':
    main()
