# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
import pprint

# Date time for arrival information
import datetime


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
    url = f"https://api-v3.mbta.com/predictions?filter[stop]={station_id}"
    response_data = get_json(url)

    if response_data['data']:
        # Get predicted arrival time
        try:
            next_arrival_time = response_data['data'][0]['attributes']['arrival_time']
            # convert arrival time to python datetime object
            arrival_time = datetime.datetime.fromisoformat(next_arrival_time)
            # # Get current time
            now = datetime.datetime.now(datetime.timezone.utc)
            # # calc time till arrival
            time_until_arrival = int((now - arrival_time).total_seconds() / 60)
            # return the time in minutes
            return time_until_arrival
        except ValueError:
            return "No ETA Prediction Available"
        except TypeError:
            return "No ETA Prediction Available"
    else:
        return "No ETA Prediction Available"


def get_nearest_station(longitude: str, latitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.

    wheelchair_code = {No Data: 0, Accessible: 1, Not Accessible: 2}
    vehicle_code = {'Unknown': 0, 'Light Rail': 1,
                    'Heavy Rail': 2, 'Commuter Rail': 3, 'Bus': 4, 'Ferry': 5}

    """
    vehicle_code = {'Unknown': 0, 'Light Rail': 1,
                    'Heavy Rail': 2, 'Commuter Rail': 3, 'Bus': 4, 'Ferry': 5}

    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    response_data = get_json(url)
    if response_data['data']:
        first_stop = response_data['data'][0]
        pprint.pprint(first_stop)
        # Gets station name
        station_name = first_stop['attributes']['name']
        # Gets BOOL if station if wheelchair accessible (True =Accessible)
        # THERE is dictionary with more in depth key - HOWEVER instructions ask for BOOL
        wheelchair_accessible = first_stop['attributes']['wheelchair_boarding'] == 1
        # Compares vehicle code to key and returns STR
        vehicle_type = vehicle_code.get(
            first_stop['attributes']['vehicle_type'], "Unknown")
        # stores station ID to use in get_predictions()
        try:
            station_id = first_stop['relationships']['zone']['data']['id']
        except:
            station_id = first_stop['relationships']['parent_station']['data']['id']
        
        time_until_arrival = get_predictions(station_id)
        return station_name, wheelchair_accessible, vehicle_type, time_until_arrival
    else:
        return f"There is no stop nearby ({longitude}, {latitude}), please choose another location"


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You can test all the functions here
    """
    location = "TD Gardens"
    print("-"*25)
    print(location)
    print(get_lat_long(location))
    # latitude, longitude = get_lat_long(location)
    # print(get_nearest_station(latitude, longitude))
    station_name, wheelchair_accessible, vehicle_type, time_until_arrival = find_stop_near(location)
    print(station_name)
    print(get_lat_long(station_name))
    


if __name__ == '__main__':
    main()
