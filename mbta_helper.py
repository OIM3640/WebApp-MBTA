# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY

TOKEN = "pk.eyJ1IjoienlhbmczIiwiYSI6ImNsdWtoY2c0djBwNjkyam1qaDIzOGxwNHEifQ.-i1DfUI64pspA8nUrJU6eg"
API_KEY = "ad31559715e24741b45b8a986ce62672"


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = TOKEN

query = "Babson College"
query = query.replace(
    " ", "%20"
)  # In URL encoding, spaces are typically replaced with "%20". You can also use urllib.parse.quote function.
url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
# print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request,

    return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
        # pprint.pprint(response_data)
    return response_data


# pprint.pprint(get_json(url))


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address,

    return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = place_name
    query = query.replace(
        " ", "%20"
    )  # In URL encoding, spaces are typically replaced with "%20". You can also use urllib.parse.quote function.
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"

    response_data = get_json(url)

    result = tuple(response_data["features"][0]["geometry"]["coordinates"][::-1])
    return result


# print(get_lat_lng("Babson College"))


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings,

    return a (station_name, wheelchair_accessible) tuple for

    the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.

    Value of Wheelchair Meaning:
    0	No Information
    1	Accessible (if trip is wheelchair accessible)
    2	Inaccessible
    """
    url = f"https://api-v3.mbta.com/stops?api_key={API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"

    response_data = get_json(url)
    # pprint.pprint(response_data)

    if len(response_data["data"]) == 0:
        return f"There isn't any MBTA station nearby."
    else:
        name = response_data["data"][0]["attributes"]["name"]
        wheelchair = response_data["data"][0]["attributes"]["wheelchair_boarding"]
        return (name, wheelchair)


# Test
# print(get_lat_lng("Boston College"))
# pprint.pprint(get_nearest_station(42.3358655, -71.1694295))
# pprint.pprint(get_nearest_station(42.2981925, -71.263598))


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address,

    return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    index1 = get_lat_lng(place_name)[0]
    index2 = get_lat_lng(place_name)[1]
    # print(index1,index2)
    return get_nearest_station(index1, index2)


# Test
# print(find_stop_near("Boston College"))


def main():
    """
    You should test all the above functions here
    """
    # json for Babson College
    print(f"\njson for Babson College")
    pprint.pprint(get_json(url))

    # Coordinate for Boston College
    print(f"\nCoordinates for Babson College")
    print(get_lat_lng("Boston College"))

    # Nearest Station for Babson College
    print(f"\nNearest MBTA Station for Boston College")
    print(get_nearest_station(42.3358655, -71.1694295))

    # Nearest Station for Babson College
    print(f"\nNearest MBTA Station for Babson College")
    print(get_nearest_station(42.2981925, -71.263598))

    # Find nearest Station for Harvard University
    print(f"\nNearest MBTA Station for Harvard University")
    print(find_stop_near("Harvard University"))


if __name__ == "__main__":
    main()
