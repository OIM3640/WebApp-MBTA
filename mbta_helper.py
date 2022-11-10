from urllib import response
import urllib.request
import json
from config import MAPQUEST_API_KEY, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# MAPQUEST_API_KEY = 'mkzRo6ydiaROmfkynLzaWHPDWB3tnRZW'
# MBTA_API_KEY = 'e3848735835b4472979ba8f2dfeabc46'

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
    place_name = place_name.split()
    place = '%20'.join(place_name)
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place}'
    data = get_json(url)
    lat_long_dict = data['results'][0]['locations'][0]['displayLatLng']
    lat, long = lat_long_dict.values()
    lat_long = lat, long
    return lat_long


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    lat = str(latitude)
    long = str(longitude)
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={long}'
    data = get_json(url)
    station_name = data["data"][0]["attributes"]["name"]
    wheelchair_accessible = data["data"][0]["attributes"]["wheelchair_boarding"]
    if wheelchair_accessible == 1:
        return (station_name, "Accessible by Wheelchair")
    if wheelchair_accessible == 0:
        return (station_name, "Not Accessible by Wheelchair")


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    This function might use all the functions above.
    Returns ((Location, Accessible), Error)
    """

    if ',' not in place_name:
        return ((None, None), True)

    lat, lng = get_lat_long(place_name)

    return (get_nearest_station(lat, lng), False)


def main():
    """
    You can test all the functions here
    """
    print(find_stop_near(("Prudential Center, Boston")))


if __name__ == '__main__':
    main()
