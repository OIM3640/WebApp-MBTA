# Your API KEYS (you need to use your own keys - very long random characters)
import json
import pprint
import urllib.request
from config import MAPBOX_TOKEN, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(
    geomapping: bool, place_name: str = None, latitude=None, longitude=None
) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.

    geomapping: bool, true if you want to find latitude and longitude
    place_name: str, the place name of the location you want to search for
    latitude: float, latitude number
    longitude: longitude number
    """

    if geomapping:
        query = place_name
        query = query.replace(
            " ", "%20"
        )  # In URL encoding, spaces are typically replaced with "%20"
        url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    else:
        url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)

    return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    df = get_json(geomapping=True, place_name=place_name)

    if not df["features"]:
        return "Cannot find latitude and longitude for this address"

    longitude, latitude = (
        df["features"][1]["center"][0],
        df["features"][1]["center"][1],
    )

    return longitude, latitude


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """

    response_data = get_json(geomapping=False, latitude=latitude, longitude=longitude)

    if not response_data["data"]:
        print("No station found")
        return exit()

    with open('mbta_response_data.json', 'w') as file:
            json.dump(response_data, file, indent=4) # For testing purpose, print to a seperate file

    station_name = response_data["data"][0]["relationships"]["parent_station"]["data"][
        "id"
    ]

    return station_name


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """

    longitude, latitude = get_lat_long(place_name)

    response_data = get_json(geomapping=False, latitude=latitude, longitude=longitude)
    
    stop_name, wheelchair_accessible = (
        response_data["data"][0]["attributes"]["name"],
        response_data["data"][0]["attributes"]["wheelchair_boarding"],
    )

    return stop_name, wheelchair_accessible


def main():
    """
    You should test all the above functions here
    """
    place_name = "Boston Common"  # Change to other places you want
    longitude, latitude = get_lat_long(place_name)
    print(get_nearest_station(latitude, longitude))
    print(find_stop_near(place_name))


if __name__ == "__main__":
    main()
