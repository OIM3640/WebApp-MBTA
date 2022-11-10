# Your API KEYS (you need to use your own keys - very long random characters)

from config import MAPQUEST_API_KEY,MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

import json
import urllib.request
from pprint import pprint

# A little bit of scaffolding if you want to use it


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
    place_name = place_name.replace("", "%20")
    url = MAPQUEST_BASE_URL + f'?key={MAPQUEST_API_KEY}&location={place_name}'
    return url
    #response_data = get_json(url)
    #lat = response_data['results'][0]['locations'][0]['showLatLng']['lat']
    #long = response_data['results'][0]['locations'][0]['showLatLng']['lng']
    #return(lat,long)

print(get_lat_long('Boston'))


   

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = MBTA_BASE_URL + f'?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongtitude%5D={longitude}'
    response_data = get_json(url)
    station = response_data['data'][0]['attributes']['name']
    wheelchair_access = response_data['data'][0]['attributes']['wheelchair_boarding']
    return(station, wheelchair_access)

    


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    station, wheelchair_access = get_nearest_station(latitude, longitude)
    if wheelchair_access == 1:
        wheelchair_access = True
    else:
        wheelchair_access = False
    return(station, wheelchair_access)
    


def main():
    """
    You can test all the functions here
    """
    place_name = 'Boston%20Common,MA'
    print(get_lat_long(place_name))
    


if __name__ == '__main__':
    main()
