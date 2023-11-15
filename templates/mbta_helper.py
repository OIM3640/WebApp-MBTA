import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = "pk.eyJ1IjoieGh1NiIsImEiOiJjbG94NTI5c2gwYXkzMnFwaXRvcW44NGtwIn0.0OUOBgmbdqbT3kxVMhdb5A"
query = "Babson College"
query = query.replace(
    " ", "%20"
)  # In URL encoding, spaces are typically replaced with "%20"
url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
# print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    MAPBOX = json.loads(response_text)
    # pprint.pprint(response_data)


MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

import requests


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    response = requests.get(url)
    d = response.json()
    return d


# print (get_json(MBTA_BASE_URL))
MBTA = get_json(MBTA_BASE_URL)


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    d = MAPBOX
    l = len(d["features"])
    for i in range(l - 1):
        if place_name in d["features"][i]["place_name"]:
            latitude = str(d["features"][i]["geometry"]["coordinates"][1])
            longitude = str(d["features"][i]["geometry"]["coordinates"][0])
            return (latitude, longitude)


# for k in MAPBOX['features'][0].keys():
#     print (k)
# print (MAPBOX['features'][0])
# print (get_lat_long('Babson College'))


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    d = MBTA
    latitude = float(latitude)
    longitude = float(longitude)
    l = len(d["data"])
    for i in range(l - 1):
        if (
            d["data"][i]["attributes"]["latitude"] == latitude
            and d["data"][i]["attributes"]["longitude"] == longitude
        ):
            if d["data"][i]["attributes"]["wheelchair_boarding"] == 1:
                return (d["data"][i]["attributes"]["name"], True)
            else:
                return (d["data"][i]["attributes"]["name"], False)


# print (type(MBTA['data'][0]['attributes']['latitude']))
# print (type(MBTA['data'][0]['attributes']['wheelchair_boarding']))
# print (get_nearest_station('42.425322', '-71.189411'))


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    t = get_lat_long(place_name)
    return get_nearest_station(t[0], t[1])


def main():
    """
    You should test all the above functions here
    """
    pass


if __name__ == "__main__":
    main()
