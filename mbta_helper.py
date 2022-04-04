# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
# MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
# MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    text = f.read().decode("utf-8")
    data = json.loads(text)
    return data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(" ", "%20")
    data = get_json(
        f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name},MA"
    )
    lat_long = data["results"][0]["locations"][0]["latLng"]
    lat_long = tuple(lat_long.values())
    return lat_long


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    MBTA_data = get_json(
        f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    )  # LINK WONT WORK WHEN I PLACE MY API KEY
    MBTA_station = MBTA_data["data"][0]["attributes"]["name"]
    wheelchair = MBTA_data["data"][0]["attributes"]["wheelchair_boarding"]
    if wheelchair == 1:
        wheelchair_status = "Available"
    elif wheelchair == 2:
        wheelchair_status = "Not Available"
    return (MBTA_station, wheelchair_status)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat_long = get_lat_long(place_name)
    return get_nearest_station(lat_long[0], lat_long[1])


def main():
    """
    You can test all the functions here
    """
    # print(get_lat_long('Boston'))
    # print(get_nearest_station(42.358894,-71.056742))
    # print(find_stop_near("Prudential Center"))


if __name__ == "__main__":
    main()
