# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
from config import OPENWEATHERMAP_APIKEY
import json
from pprint import pprint
MAPBOX_TOKEN = 'pk.eyJ1IjoiYWJpcnNldGhpIiwiYSI6ImNsZnpzbjZyMTBhc3EzbXFwdnV2enNoZ3YifQ.50Xh5oJ7YoMHk8Aq5aMNiQ'
MBTA_API_KEY = '44abdcab5e6a4c01afbae2d0b846fb20'

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
# query = 'Babson%20College'
# mapbox_url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'

# A little bit of scaffolding if you want to use it


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.
    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    url = url.replace(' ', '%20')
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.
    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    mapbox_url = f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi'
    # print(mapbox_url)
    response_data = get_json(mapbox_url)
    coordinates = response_data['features'][0]['geometry']['coordinates']
    return coordinates



def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """

    # MBTA_url = f"{MBTA_BASE_URL}?filter[route_type]=0&include=wheelchair_boarding&fields[stop]=name,latitude,longitude,wheelchair_boarding&sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}&api_key={MBTA_API_KEY}"
    MBTA_url = f"{MBTA_BASE_URL}?sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}&api_key={MBTA_API_KEY}"
    response_data = get_json(MBTA_url)
    nearest_station = response_data["data"][0]
    station_name = nearest_station ["attributes"]["name"]
    wheelchair_accessible = nearest_station["attributes"]["wheelchair_boarding"] == "1"

    return station_name, wheelchair_accessible


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    This function might use all the functions above.
    """
    coordinates = get_lat_long(place_name)
    lat, long = coordinates
    station_name, access = get_nearest_station(long,lat)
    return station_name, access
    # print(f'The nearest station is {station_name} and the wheel chair access is {access}')

def get_temp(city: str) -> float:
    """
    return the current temperature of a given city
    """
    city = city.replace(' ', '%20')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={OPENWEATHERMAP_APIKEY}&units=metric'
    print(url)

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        # print(response_text)
        response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    return response_data['main']['temp']



def main():
    """
    You can test all the functions here
    """
    find_stop_near('Fenway boston')

    pass


if __name__ == '__main__':
    main()