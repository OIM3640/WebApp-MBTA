# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY

import pprint
import json
import urllib.request
import urllib.parse

MAPBOX_TOKEN

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

query = 'Babson College'
query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url) # Try this URL in your browser first

# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data

# pprint.pprint(get_json(url))

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    # get mapbox dictionary
    query = place_name
    query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    mapbox_dict = get_json(url)
    lat, long = mapbox_dict['features'][0]['center']

    return lat, long

# print(get_lat_long('Babson College'))

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    sorting = 'distance'
    params = urllib.parse.urlencode({'filter[latitude]': longitude, 'filter[longitude]': latitude, 'page[limit]': 1, 'sort': sorting})
    url = '?'.join((MBTA_BASE_URL,params))
    
    nearest_station = get_json(url)
    station_name = nearest_station['data'][0]['attributes']['name']
    wheelchair_value = nearest_station['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair_value == 1:
        wheelchair_accessible = True
    else: 
        wheelchair_accessible = False
    return station_name, wheelchair_accessible



def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat, long = get_lat_long(place_name)
    return get_nearest_station(lat, long)



def main():
    """
    You should test all the above functions here
    """
    print(find_stop_near('Boston Common'))


if __name__ == '__main__':
    main()
