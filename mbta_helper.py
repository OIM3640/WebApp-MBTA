# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY, place_name_inp

import json
import urllib.request
import urllib.parse


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        return json.loads(response_text)
        

    


def get_lat_long(place_name_inp: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = urllib.parse.quote(place_name_inp)
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    response_data = get_json(url)

    if 'features' in response_data and response_data['features']:
        first_feature = response_data['features'][0]
        if 'center' in first_feature: # WHYYYYYYYY
            return tuple(map(str, first_feature['center'])) ## feature is in the context of the geographical entities or locations returned in the API response 
    
    return None



def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    map_url = f'{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}'
    response_data_station = get_json(map_url)

    if 'data' in response_data_station and response_data_station['data']:
        closest_station = response_data_station['data'][0]['attributes']['name']
        wheelchair_accessible = response_data_station['data'][0]['attributes']['wheelchair_boarding'] == 1
        return closest_station, wheelchair_accessible

    return None

    


def find_stop_near(place_name_inp: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    coordinates = get_lat_long(place_name_inp)

    if coordinates:
        latitude, longitude = coordinates
        return get_nearest_station(latitude, longitude)

    return None


def main():
    """
    You should test all the above functions here
    """
    result = find_stop_near(place_name_inp)

    if result:
        station_name, wheelchair_accessible = result
        print(f"The nearest MBTA stop to {place_name_inp} is {station_name}.")
        print(f"Wheelchair Accessible: {wheelchair_accessible}.")


if __name__ == '__main__':
    main()
