# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
import pprint

# Date time for arrival information
import requests
from datetime import datetime


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# A little bit of scaffolding if you want to use it


def get_url(place: str):
    """
    Given the name of a place, return a Map Box url
    """
    query = place.replace(" ", "%20")
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    return url


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url = get_url(place_name)
    response_data = get_json(url)
    longitude, latitude = response_data['features'][0]['center']
    latitude = round(latitude, 4)
    longitude = round(longitude, 4)
    return longitude, latitude


def get_predictions(station_id: str) -> str:
    '''
    Given station ID, return the predicted arrival time of next vehicle

    '''
    url = f"https://api-v3.mbta.com/predictions?filter%5Bstop%5D={station_id}&sort=arrival_time&direction_id=0&api_key={MBTA_API_KEY}"
    print(url)
    response_data = get_json(url)

    if response_data['data']:
        # Get predicted arrival time
        next_arrival_time = response_data['data'][0]['attributes']['arrival_time']
        # convert arrival time to python datetime object
        arrival_time = datetime.fromisoformat(next_arrival_time)
        # Get current time
        now = datetime.now()
        # calc time till arrival
        time_until_arrival = arrival_time - now
        # return the time in minutes
        return time_until_arrival.total_seconds()//60
    else:
        return "No ETA Prediction available"


def get_nearest_station(longitude: str, latitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.

    wheelchair_code = {}
    vehicle_code = {}

    """
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    response_data = get_json(url)
    if response_data['data']:
        first_stop = response_data['data'][0]
        pprint.pprint(first_stop)
        station_name, wheelchair_accessible, vehicle_type = first_stop['attributes'][
            'name'], first_stop['attributes']['wheelchair_boarding'], first_stop['attributes']['vehicle_type']
        if wheelchair_accessible == 1:
            wheelchair_accessible = True
        else:
            wheelchair_accessible = False
        station_id = first_stop['id']
        time_until_arrival = get_predictions(station_id)
        return station_name, wheelchair_accessible, vehicle_type, time_until_arrival
    else:
        return f"There is no stop nearby ({longitude}, {latitude}), please choose another location"


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    longitude, latitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You can test all the functions here
    """
    # url = get_url("Babson College")
    # pprint.pprint(get_json(url))
    location = "Boston Commons"
    print(location)
    print(get_lat_long(location))
    longitude, latitude = get_lat_long(location)
    print(get_nearest_station(longitude, latitude))
    # print(get_nearest_station(get_lat_long(location)))
    # print(find_stop_near(location))


if __name__ == '__main__':
    main()
