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


pprint.pprint(get_json(url))


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

    result = tuple(response_data["features"][0]["geometry"]["coordinates"])
    return result


print(get_lat_lng("Babson College"))


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings,

    return a (station_name, wheelchair_accessible) tuple for

    the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"https://api-v3.mbta.com/stops?api_key={API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"

    response_data = get_json(url)

    # print(response_data)

    if len(response_data["data"]) == 0:
        # url1 = f"https://api-v3.mbta.com/stops?api_key={API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&filter[radius]={100}&sort=distance"
        # response_data = get_json(url1)

        # name = response_data["data"][0]["attributes"]["name"]
        # wheelchair = response_data["data"]["attributes"]["wheelchair_boarding"]
        # return name, wheelchair
        return f"There isn't any MTBA station nearby."
    else:
        name = response_data["data"][0]["attributes"]["name"]
        wheelchair = response_data["data"]["attributes"]["wheelchair_boarding"]
        return name, wheelchair


print(get_nearest_station(-71.263598, 42.2981925))
print(get_lat_lng("Boston College"))
print(get_nearest_station(-71.1694295, 42.3358655))


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address,

    return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You should test all the above functions here
    """
    pass


if __name__ == "__main__":
    main()
