# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


import urllib.request
import json
from pprint import pprint


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    url = MAPQUEST_BASE_URL + f'?key={MAPQUEST_API_KEY}&location={place_name}'
    response_data = get_json(url)
    lat = response_data['results'][0]['locations'][0]['displayLatLng']['lat']
    long = response_data['results'][0]['locations'][0]['displayLatLng']['lng']
    return (lat,long)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = MBTA_BASE_URL + f'?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    response_data = get_json(url)
    station_name = response_data['data'][0]['attributes']['name']
    wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding']
    return (station_name, wheelchair_accessible)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    station_name, wheelchair_accessible = get_nearest_station(latitude, longitude)
    if wheelchair_accessible == 1:
        wheelchair_accessible = True
    else:
        wheelchair_accessible = False
    return (station_name, wheelchair_accessible)
   

def main():
    """
    You can test all the functions here
    """
    # place_name = 'Boston%20Common,MA'
    # print(get_lat_long(place_name))

    # latitude = 42.37401
    # longitude = -71.06005
    # print(get_nearest_station(latitude, longitude))

    place_name = 'Boston%20Common,MA'
    print(find_stop_near(place_name))

if __name__ == '__main__':
    main()