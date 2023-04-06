"""
We attempted to add a map to our project but did not get it to work. 
Here is some of the code that we build for the map.
"""
from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
import pprint

from mbta_helper import get_json, get_lat_long, get_nearest_station

def get_station_coords(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given the latitute and longitude strings, return a (station_lat, station_lng) tuple 
    for the nearest MBTA station to the given coordinates.
    """
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    response_data = get_json(url)
    if response_data['data']:
        first_stop = response_data['data'][0]
        # Gets station name
        station_lat, station_lng = first_stop['attributes']['latitude'],first_stop['attributes']['longitude']
        return station_lat, station_lng
    else:
        return f"There is no stop nearby ({latitude}, {longitude}), please choose another location"

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    if get_nearest_station(latitude, longitude) == get_station_coords(latitude, longitude):
        return f"There is no stop nearby ({latitude}, {longitude}), please choose another location"
    else:
        station_name, wheelchair_accessible, vehicle_type, time_until_arrival = get_nearest_station(latitude, longitude)
        station_lat, station_lng = get_station_coords(latitude, longitude)
    return station_name, wheelchair_accessible, vehicle_type, time_until_arrival, station_lat, station_lng

def main():
    location = "Boston Commons"
    print("-"*25)
    print(location)
    print(get_lat_long(location))
    latitude, longitude = get_lat_long(location)
    print(get_station_coords(latitude, longitude))
    print("-" * 75)
    print(find_stop_near(location))
    
if __name__ == '__main__':
    main()