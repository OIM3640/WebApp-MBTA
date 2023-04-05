"""LUKE PATA"""
# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY
from pprint import pprint
import json
import urllib.request
import math

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1IjoibHBhdGExIiwiYSI6ImNsZzB5emJrbjFmemEzZHA2N3hyd2phZW4ifQ.PC064m-1E2K0hxfFHYVZzQ"
WEATHER_API_KEY = "73d8abd2d39ba8d8aa4276f9b3bb61e3"

# query = 'Babson%20College'
# url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url)

# with urllib.request.urlopen(url) as f:
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#     pprint(response_data)
# print(response_data['features'][0]['properties']['address'])

# A little bit of scaffolding if you want to use it

MBTA_API_KEY = 'fe1a052ac7a146ab99013a71e70f5167'


def get_json(location) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    # Write a function that takes an address or place name as input and returns a properly encoded URL to make a Mapbox geocoding request.
    location = location.replace(" ", "%20")
    # urllib.parse.urlencode(query=location, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)   #Tried with not muhc success (Would retry in future but got confused)
    url = f'{MAPBOX_BASE_URL}/{location}.json?access_token={MAPBOX_TOKEN}&types=poi'
    # print(url)
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint(response_data)
        return response_data


# def get_lat_long(place_name: str) -> tuple[str, str]:
def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    data = get_json(place_name)  # lat should be pos and long negative
    # print(data['features'][0]['geometry']['coordinates'])
    long_lat_tuple = tuple(data['features'][0]['geometry']['coordinates'])
    return long_lat_tuple


# def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
def get_nearest_station(latitude_longitue) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    # long_lat_tuple = get_lat_long()
    latitude = str(latitude_longitue[1])
    longitude = str(latitude_longitue[0])
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    # print(url)
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint(response_data)
    # pprint(response_data['data'])
    try:
        stop_name = response_data['data'][0]['attributes']['name']
        wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding']
        name_accessible = (stop_name, wheelchair_accessible)
        return name_accessible
    except IndexError:
        return "Problem"


def get_temp(city):
    """
    This function gets the current temp of the area for the output after location and accessiblity.
    """
    APIKEY = WEATHER_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={APIKEY}&units=imperial'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data['main']['temp']


# def find_stop_near(place_name: str) -> tuple[str, bool]:
def find_stop_near(name_accessible) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    name_accessible_tuple = get_nearest_station()
    temp = get_temp("Boston")
    if name_accessible_tuple == "Problem":
        return ['There was an Error']
        # return f'There was an error, please try a differnet location, thank you. The temperature is {temp} degrees fahrenheit.'
    else:
        pass
    stop_name = name_accessible_tuple[0]
    # print(stop_name)
    wheelchair_accessible = name_accessible_tuple[1]
    # print(wheelchair_accessible)
    if wheelchair_accessible == 0:
        return (stop_name, 'no information', temp)
        # return f'{stop_name} is the closest stop, with sadly no information on wheelchair accessibility.'
    elif wheelchair_accessible == 1:
        return (stop_name, 'is wheelchair accessible', temp)
        # wheelchair_accessible = 'accessible'
    else:
        return (stop_name, 'is not wheelchair acccessible', temp)
        # wheelchair_accessible = 'inaccessible'
        # return f'{stop_name} is the closest MBTA stop and it is {wheelchair_accessible} for wheelchair use. The temperature is {temp} degrees fahrenheit.'


def main():
    """
    You can test all the functions here
    """
    # get_json()
    # print(get_lat_long())
    # print(get_nearest_station())
    # print(get_temp())
    print(find_stop_near())


if __name__ == '__main__':
    main()
