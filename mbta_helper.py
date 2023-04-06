#disabling SSL certificate verification - resolve error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Handling Error
from urllib.error import HTTPError

# Your API KEYS (you need to use your own keys - very long random characters)
from pprint import pprint
import json
import urllib.request
import requests

# Useful URLs (you need to add the appropriate parameters for your requests)
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_API_KEY = '921c13397cb140b2aaf7b840c81c8bc2'
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1IjoibGlseWljaGlzZSIsImEiOiJjbGZ5Y2s3a20wcHV6M2RwNmhiZ24zY2xpIn0.tdctb2NgGOa8Sb1out2BRg'
# query = 'Babson%20College'
# url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url)  # Try this URL in your browser first

# with urllib.request.urlopen(url) as f:
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#    pprint(response_data)
# A little bit of scaffolding if you want to use it


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.

        - The imported 'requests' library is used to send an HTTP request to the API endpoint specified in the URL.
        - 'response.json()' is used to extract JSON data from the response.
        - The JSON data is finally returned as a dictionary.
    """
    response = requests.get(url)
    json_data = response.json()
    return json_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
Given a place name or address, return a(latitude, longitude) tuple with the coordinates of the given place.

See https: // docs.mapbox.com/api/search/geocoding / for Mapbox Geocoding API URL formatting requirements.
"""
    #place_name + place_name + " massachusetts"
    # Build the URL for the Mapbox Geocoding API endpoint
    url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}"

    # Send an HTTP GET request to the API endpoint
    response_data = get_json(url)

    # Extract the latitude and longitude coordinates from the response data
    try:
        latitude = str(response_data["features"][0]["center"][1])
        longitude = str(response_data["features"][0]["center"][0])
        return latitude, longitude
    except (IndexError, KeyError):
        # Return None if the response data doesn't contain the required information
        return None, None


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
Given latitude and longitude strings, return a(station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

# /Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
See https: // api-v3.mbta.com/docs/swagger/index.html
"""
    # Build the URL for the MBTA API endpoint
    # start with the MBTA base url, filter the data by latitude and longitude, then sort by the distance and specify the api key required to access the MBTA API
    url = f"{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}"

    # Send an HTTP GET request to the API endpoint
    response_data = get_json(url)

    # Extract the station name and wheelchair accessibility from the response data
    try:
        station_name = response_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1
        return station_name, wheelchair_accessible
    except (IndexError, KeyError):
        # Return None if the response data doesn't contain the required information
        return None, None


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

This function might use all the functions above.
"""
    # get the latitude and longitude of the given place
    latitude, longitude = get_lat_long(place_name)

    if latitude is not None and longitude is not None:
        # Get the nearest MBTA stop and whether it is wheelchair accessible
        return get_nearest_station(latitude, longitude)
    else:
        # Return None if the latitude and longitude couldn't be determined.
        return None, None

#My weather API key
OPENWEATHERMAP_APIKEY = 'bd934d1c567130b31d6bebfff8abab04'


# def weather(place_name: str) -> float:
#     """ 
#     This function gets the weather of the inputed city
#     """
#     place_name = place_name.replace(' ', '%20')
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={place_name},us&APPID={OPENWEATHERMAP_APIKEY}&units=metric'
#     # print(url)

#     with urllib.request.urlopen(url) as f:
#         response_text = f.read().decode('utf-8')
#         response_data = json.loads(response_text)
#     # pprint.pprint(response_data)
#     return response_data['main']['temp']

#New weather function accounting for error:
def weather(place_name: str) -> float:
    """ 
    This function gets the weather of the inputed city
    """
    place_name = place_name.replace(' ', '%20')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={place_name},us&APPID={OPENWEATHERMAP_APIKEY}&units=metric'
    # print(url)

    try:
        with urllib.request.urlopen(url) as f:
            response_text = f.read().decode('utf-8')
            response_data = json.loads(response_text)
        # pprint.pprint(response_data)
        return response_data['main']['temp']
    except HTTPError as e:
        print(f"HTTPEttrror: {e}")
        return "not available for this location"


def main():
    """
You can test all the functions here
"""
    place_name = input("Enter a place name or address: ")
    stop_name, wheelchair_accessible = find_stop_near(place_name)
    if stop_name is not None and wheelchair_accessible is not None:
        print(
            f"The nearest MBTA stop to {place_name} is {stop_name}. Wheelchair accessibility: {wheelchair_accessible}")
    else:
        print("Nearest MBTA stop not found.")

    print(
        f"The weather in {place_name} is {weather(place_name)} degrees Celcius.")


if __name__ == '__main__':
    main()
