# Your API KEYS (you need to use your own keys - very long random characters)
#from config import MAPBOX_TOKEN, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

import requests
import mbta_helper
print(mbta_helper.find_stop_near("Boston Common"))

import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1IjoiYWxpY2VtaW5rb3YiLCJhIjoiY2xvcHltYmxwMGNvNzJpcDh0dHNqZm11NyJ9.xNfkWDYkZMEL_MiqHpHK-w'
query = 'Boston Logan Airport'
query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint.pprint(response_data)
print(response_data['features'][0]['properties']['address'])

print(mbta_helper.find_stop_near("Boston Logan Airport"))


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    response = requests.get(url)
    json_data = response.json()
    return json_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/Boston%20Logan%20Airport.json?access_token=pk.eyJ1IjoiYWxpY2VtaW5rb3YiLCJhIjoiY2xvcHltYmxwMGNvNzJpcDh0dHNqZm11NyJ9.xNfkWDYkZMEL_MiqHpHK-w'
    print(url)
    
    if 'features' in get_json(url):
        coordinates = get_json(url)['features'][0]['geometry']['coordinates']
        latitude, longitude = coordinates[1], coordinates[0]
        return latitude, longitude

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    api_key = '4dab2290df5542b18165131a46cc26bb'
    latitude = '-71.027584'
    longitude = '42.366148'

    url=('https://api-v3.mbta.com/stops?api_key={api_key}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}')

    #print(url=('https://api-v3.mbta.com/stops?api_key={4dab2290df5542b18165131a46cc26bb}&sort=distance&filter%5Blatitude%5D={-71.027584}&filter%5Blongitude%5D={42.366148}'))

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """

    coordinates = get_lat_long(place_name)

    if coordinates:
        # Construct the URL for the MBTA stops API with the latitude and longitude
        url = f'https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D=-71.027584&filter%5Blongitude%5D=42.366148&api_key=4dab2290df5542b18165131a46cc26bb'

        stops_data = get_json(url)

    if stops_data and 'data' in stops_data and stops_data['data']:
        nearest_stop = stops_data['data'][0]['attributes']['name']
        wheelchair_accessible = stops_data['data'][0]['attributes']['wheelchair_boarding'] == 1

        print(nearest_stop, wheelchair_accessible)

def main():
    """
    You should test all the above functions here
    """
    print(get_json('https://api.mapbox.com/geocoding/v5/mapbox.places/Boston%20Logan%20Airport.json?access_token=pk.eyJ1IjoiYWxpY2VtaW5rb3YiLCJhIjoiY2xvcHltYmxwMGNvNzJpcDh0dHNqZm11NyJ9.xNfkWDYkZMEL_MiqHpHK-w&types=poi'))
    #print(get_lat_long('Boston Logan Airport'))
    place_name = 'Boston Logan Airport'
    latitude, longitude = get_lat_long(place_name)
    print(latitude)
    print(longitude)
    print("Near stop at:",find_stop_near('Boston Logan Airport'))
    print("Nearest Station at:", get_nearest_station(latitude, longitude))
    #nearest_stop, wheelchair_accessible = find_stop_near('Boston Logan Airport')
    #nearest_stop, wheelchair_accessible = find_stop_near(place_name)
    print(mbta_helper.find_stop_near("Boston Common"))
    
    
if __name__ == '__main__':
    main()