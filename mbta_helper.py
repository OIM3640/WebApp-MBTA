# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


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
    place_name = place_name.replace(' ', "%20")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    Latlng = get_json(url)['results'][0]['locations'][0]['displayLatLng']
    return Latlng['lat'], Latlng['lng']


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    response_data = get_json(url)
    if response_data['data'][0]['attributes']['wheelchair_boarding'] == 1:
        wheel_chair = 'Some vehicles at this stop can be boarded by a rider in a wheelchair.'
    elif response_data['data'][0]['attributes']['wheelchair_boarding'] == 0:
        wheel_chair = 'No accessibility information for the stop'
    else:
        wheel_chair = 'Wheelchair boarding is not possible at this stop'
    return response_data['data'][0]['attributes']['name'], wheel_chair


# test
lat, lng = get_lat_long('Boston College MA')
print(lat, lng)
pprint(get_nearest_station(lat, lng))

#get_nearest_station(get_lat_long('boston college')[0],get_lat_long('babson college')[1])


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat, lng = get_lat_long(place_name)
    station_name, wheelchair_accessible = get_nearest_station(lat, lng)
    return station_name, wheelchair_accessible


def main():
    """
    You can test all the functions here
    """


if __name__ == '__main__':
    main()
