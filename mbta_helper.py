# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = 'oyo5kKGI69WA0NjqYvijQTSAAq4QsBMo'
MBTA_API_KEY = '5951a02b287a4bcaa87ac1e2c37f9a75'

import urllib.request
import urllib.parse
import json
from pprint import pprint


# A little bit of scaffolding if you want to use it


def get_json(location):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(location)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    data = urllib.parse.urlencode({
        'key': MAPQUEST_API_KEY,
        'location': place_name,
    })
    url = f"{MAPQUEST_BASE_URL}?{data}"
    response_data = get_json(url)
    latitude = response_data['results'][0]['locations'][0]['displayLatLng']['lat']
    longitude = response_data['results'][0]['locations'][0]['displayLatLng']['lng']
    t = (latitude, longitude)
    return t

    

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """

    url = f'https://api-v3.mbta.com/stops?page%5Blimit%5D=1&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    station = response_data['data'][0]['attributes']['name']
    Wheelchair = response_data['data'][0]['attributes']['wheelchair_boarding']
    t = (station, Wheelchair)
    print(t)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You can test all the functions here
    """
    # print(get_lat_long("Wellesley"))
    # get_nearest_station('42.3470566', '-71.086222')
    find_stop_near("Boston College")


if __name__ == '__main__':
    main()
