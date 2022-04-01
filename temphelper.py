import urllib.request
import json
from config import OPENWEATHERMAP_APIKEY

import pprint


def get_temp(city):
    city = city.replace(' ', '%20')
    APIKEY = OPENWEATHERMAP_APIKEY
    country_code = 'us'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

    print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    temp = response_data['main']['temp']
    return round(temp - 273.15, 1)


def main():
    print(get_temp("Wellesley"))
    print(get_temp("New York"))


if __name__ == "__main__":
    main()