# Your API KEYS (you need to use your own keys - very long random characters)
from pprint import pprint
import json
import urllib.request
from config import MAPQUEST_API_KEY, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
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
    # data = pprint(response_data)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    Example shown below:
    url = f'http://mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    """
    place_name = place_name.replace(" ", "%20")
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place_name}'
    data = get_json(url)
    latitude = data['results'][0]['locations'][0]['displayLatLng']['lat']
    longitude = data['results'][0]['locations'][0]['displayLatLng']['lng']
    return latitude, longitude

# print(get_lat_long('Babson College'))


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
    Example shown below:
    curl -X GET "https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D=27.84375&filter%5Blongitude%5D=-81.53531" -H "accept: application/vnd.api+json"
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    data = get_json(url)
    # pprint(data)
    station_name = data['data'][0]['attributes']['name']
    wheelchair_accessible = data['data'][0]['attributes']['wheelchair_boarding']
    return station_name, wheelchair_accessible


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    Meaning for wheelchair accessible:
        0 --> No Information
        1 --> Accessible (if trip is wheelchair accessible)
        2 --> Inaccessible
    """
    latitude, longitude = get_lat_long(place_name)
    station_name, wheelchair_accessible = get_nearest_station(
        latitude, longitude)
    if wheelchair_accessible == 1:
        wheelchair = 'Accessible'
    elif wheelchair_accessible == 2:
        wheelchair = 'Inaccessible'
    else:
        wheelchair = 'No Information'
    return station_name, wheelchair


def main():
    """
    You can test all the functions here
    """
    # print(get_lat_long('Boston'))
    #print(get_nearest_station(42.35866, -71.05674))
    print(find_stop_near('Boston'))


if __name__ == '__main__':
    main()
