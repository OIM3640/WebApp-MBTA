import urllib.request
from pprint import pprint
import json
from config import MAPQUEST_KEY, MBTA_KEY


# Base URLs
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Our API Keys (from config).
MAPQUEST_API_KEY = MAPQUEST_KEY
MBTA_API_KEY = MBTA_KEY


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
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
    for Mapquest Geocoding  API URL formatting requirements.
    """
    # Changes all spaces to %20 so that the url can read it
    if " " in place_name:
        place_name = place_name.replace(" ", "%20")
    # Restricts area to just the Boston area
    state = "MA"
    city = "Boston"
    location = (get_json(
        f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name},{state},{city}%20"))
    # pprint(locations)
    lat_long = location['results'][0]['locations'][0]['latLng']
    lat_long = tuple(lat_long.values())
    return lat_long


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    response_data = (get_json(
        f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"))

    station = response_data["data"][0]["attributes"]['name']

    wc_inf = response_data["data"][0]["attributes"]["wheelchair_boarding"]

    # Gives us the accessibility of each station
    if wc_inf == 0:
        wc_acs = "No Wheelchair Information"
    elif wc_inf == 1:
        wc_acs = "Wheelchair accessible"
    elif wc_inf == 2:
        wc_acs = "Wheelchair inaccessible"
    return station, wc_acs


def find_stop_near(location):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """

    lat = get_lat_long(location)[0]
    long = get_lat_long(location)[1]
    return f'{get_nearest_station(lat,long)}'


def main():
    """
    Test all the functions here
    """

    place_name = input(
        "Please enter a specific location in Boston to view the nearest MBTA station and the wheelchair information: ")
    print(find_stop_near(place_name))


if __name__ == '__main__':
    main()