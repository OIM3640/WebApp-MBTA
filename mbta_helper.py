import urllib.request
import json
from pprint import pprint

# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPQUEST_API_KEY, MBTA_API_KEY
MAPQUEST_API_KEY= "vbvSagGcRQOERezgVV3BPEI4jcGvRAxG"
MBTA_API_KEY= "3e8a26a9583045e1aac5a93e4538d3d4"

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
    place_name = place_name.replace(' ', '%20')
    mapquest_url = get_json(f'https://www.mapquestapi.com/geocoding/v1/address?key=%20{MAPQUEST_API_KEY}%20&location=%20{place_name}%20,Boston,MA')
    coordinates = mapquest_url['results'][0]['locations'][0]['latLng']
    return tuple(coordinates.values())


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"'
    data = get_json(url)
    station_name = data['data'][0]['attributes']['name']
    wheelchair_accesibile = data['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair_accesibile > 0 and wheelchair_accesibile < 2:
        wheelchair_accesibile = "Wheelchair Inaccessible"
    elif wheelchair_accesibile >= 2:
        wheelchair_accesibile = "Wheelchair Accessible"
    else:
        wheelchair_accesibile = "No information available"
    return (station_name, wheelchair_accesibile)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude = get_lat_long(place_name)[0]
    longitude = get_lat_long(place_name)[1]
    return get_nearest_station(latitude, longitude)


def main():
    """
    You can test all the functions here
    """
    place = input("Please enter an address in Boston:")
    print(find_stop_near(place))


if __name__ == '__main__':
    main()
