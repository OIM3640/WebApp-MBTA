from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
import pprint

# Date time for arrival information
import datetime

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_url(place: str):
    """
    Given the name of a place, return a Map Box url
    """
    query = place.replace(" ", "%20")
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    return url


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, 
    return a Python JSON object containing the response to that request.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.
    """
    url = get_url(place_name)
    response_data = get_json(url)
    longitude, latitude = response_data['features'][0]['center']
    latitude = round(latitude, 4)
    longitude = round(longitude, 4)
    return latitude, longitude


def get_predictions(station_id: str) -> str:
    """
    Given station ID, return the predicted arrival time of next vehicle.
    """
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


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, 
    return a (station_name, wheelchair_accessible, vehicle_type, time_untill_arrival) tuple 
    for the nearest MBTA station to the given coordinates.

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
        return f"There is no stop nearby ({latitude}, {longitude}), please choose another location"

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop, whether it is wheelchair accessible,
    the vehicle type, and the time until arrival.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude) # includes station_name, wheelchair_accessible, vehicle_type, time_until_arrival


def main():
    location = "Boston Commons"
    print("-"*25)
    print(location)
    print(get_lat_long(location))
    latitude, longitude = get_lat_long(location)
    print(get_nearest_station(latitude, longitude))
    print("-" * 75)
    print(find_stop_near(location))
    

if __name__ == '__main__':
    main()
