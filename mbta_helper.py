# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import requests
import json
from urllib import parse

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    response = requests.get(url)
    return response.json()


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_name_encoded = parse.quote(place_name)  # Ensure we're using the right variable name here
    url = f"{MAPBOX_BASE_URL}/{place_name_encoded}.json?access_token={MAPBOX_TOKEN}"
    data = get_json(url)
    longitude, latitude = data['features'][0]['center']
    return str(latitude), str(longitude)


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    
    # Get the JSON response from the API
    data = get_json(url)
    
    # Extract the station name and wheelchair accessibility
    station_name = data['data'][0]['attributes']['name']
    wheelchair_accessible = data['data'][0]['attributes']['wheelchair_boarding'] == 1
    return station_name, wheelchair_accessible

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You should test all the above functions here
    """
    test_place = "Boston Common"
    station_name, is_accessible = find_stop_near(test_place)
    
    print(f"The nearest MBTA station to {test_place} is {station_name} and it is {'wheelchair accessible' if is_accessible else 'not wheelchair accessible'}.")


if __name__ == '__main__':
    main()
