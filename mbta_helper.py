# Your API KEYS (you need to use your own keys - very long random characters)
import urllib.parse
import urllib.request
from config import MAPBOX_TOKEN, MBTA_API_KEY
import json
from pprint import pprint

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
        response_data = json.loads(response_text)
        return response_data



def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    #urllib.parse converts the user string input into url form 
    query = urllib.parse.quote_plus(place_name, safe='', encoding=None, errors=None)
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'

    #call the function get_json to return json object
    json_output = get_json(url)

    #this function will return a tuple of the geometric coordinates of the user's location
    #IMPORTANT!!! the output returns [Longitude, Latitude] <- we need to switch this over to get the nearest station!!!
    return json_output['features'][0]['geometry']['coordinates']


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    URL = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    json_output = get_json(URL)
    pprint((json_output['data'][0]['attributes']['name'],json_output['data'][0]['attributes']['wheelchair_boarding']))


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You can test all the functions here
    """
    # print(get_lat_long('Harvard University'))
    print(get_nearest_station(42.3737614375,-71.1181085))


if __name__ == '__main__':
    main()
