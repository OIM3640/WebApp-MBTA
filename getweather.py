import urllib.request
import json
import pprint
from config import OPENWEATHERMAP_APIKEY
from mbta_helper import get_lat_long, get_json

def get_info(city):
    (lon, lat) = get_lat_long(city)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHERMAP_APIKEY}&units=metric'
    response_data = get_json(url)
    return response_data

def get_temp(city: str) -> float:
    """
    return the current temperature of a given city
    """
    return get_info(city)['main']['temp']

def get_cityid(city):
    '''
    Returns the city id of the given city
    '''
    return get_info(city)['id']

def main ():
    print(get_temp('wellesley'))
    print(get_cityid('Wellesley'))

if __name__ == "__main__":
    main()