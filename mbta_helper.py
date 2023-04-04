# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN , MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
import urllib.request
import json
from pprint import pprint


def get_json(url):  # finished
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    res_text = f.read().decode("utf-8")
    res_data = json.loads(res_text)
    return res_data


def get_lat_long(place_name):  # need to work on the url
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    adjusted_place = place_name.replace(" ", "%20")
    url = f'{MAPBOX_BASE_URL}/{adjusted_place}.json?access_token={MAPBOX_TOKEN}&types=poi'
    information = get_json(url)
    longtitude, latitude = information["features"][0]["center"]
    return (longtitude, latitude)

def wheelchair_accessibility(num):
    if num == 0:
        return "No Information"
    elif num == 1:
        return "Accessible"
    elif num == 2:
        return "Inaccessible"
    
def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    information = get_json(url)["data"][0]["attributes"]
    station = information["name"]
    wheelchair = wheelchair_accessibility(information["wheelchair_boarding"])
    return (station, wheelchair)


def find_stop_near(place_name) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    longtitude, latitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longtitude)


def main():
    """
    You can test all the functions here
    """
    print(find_stop_near("Boston Common"))


if __name__ == "__main__":
    main()
