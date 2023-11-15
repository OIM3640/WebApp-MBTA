# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY

import json
import urllib.request
import urllib.parse

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request,
    return a Python JSON object containing the response to that request.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        return json.loads(response_text)


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    """
    query = urllib.parse.quote(place_name)
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    response_data = get_json(url)

    if 'features' in response_data and response_data['features']:
        first_feature = response_data['features'][0]
        if 'center' in first_feature:
            return tuple(map(str, first_feature['center']))

    return None


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple
    for the nearest MBTA station to the given coordinates.
    """
    map_url = f'{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}'
    response_data_station = get_json(map_url)

    if 'data' in response_data_station and response_data_station['data']:
        closest_station = response_data_station['data'][0]['attributes']['name']
        wheelchair_accessible = response_data_station['data'][0]['attributes']['wheelchair_boarding'] == 1
        return closest_station, wheelchair_accessible

    return None


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop
    and whether it is wheelchair accessible.
    """
    coordinates = get_lat_long(place_name)

    if coordinates:
        latitude, longitude = coordinates
        return get_nearest_station(latitude, longitude)

    return None, None


def get_map_url() -> str:
    """
    Return the Mapbox WMTS URL for map integration.
    """
    return "https://api.mapbox.com/styles/v1/nguilla1/cloz94yyd00tf01qj3nj49452/wmts?access_token=pk.eyJ1Ijoibmd1aWxsYTEiLCJhIjoiY2xveGh4bXV4MTM2ZzJtcGZhOGpxY2kyZyJ9.z1jCcbODGXBMy0qbzVAHAA"


def main():
    """
    You should test all the above functions here.
    """
    place_name = input("Enter the name of a city: ")
    result = find_stop_near(place_name)

    if result:
        station_name, wheelchair_accessible = result
        print(f"The nearest MBTA stop to {place_name} is {station_name}.")
        print(f"Wheelchair Accessible: {wheelchair_accessible}.")


if __name__ == '__main__':
    main()
