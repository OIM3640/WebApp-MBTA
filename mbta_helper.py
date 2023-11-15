# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY, OPENWEATHERMAP_APIKEY
import json
import pprint
import urllib.request

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
        # pprint.pprint(response_data)
        return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = place_name
    query = query.replace(
        " ", "%20"
    )  # In URL encoding, spaces are typically replaced with "%20"
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    response_data = get_json(url)

    latitude = response_data["features"][0]["geometry"]["coordinates"][1]
    longitude = response_data["features"][0]["geometry"]["coordinates"][0]
    return latitude, longitude


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url2 = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    response_data = get_json(url2)
    # print(response_data)
    station_name = response_data["data"][0]["attributes"]["name"]
    wheelchair_accessible = (
        response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1
    )

    return station_name, wheelchair_accessible


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    station_name, wheelchair_accessible = get_nearest_station(latitude, longitude)
    wheelchair_accessible = str(wheelchair_accessible).lower()

    result = f"The nearest station to {place_name} is {station_name}. It is {wheelchair_accessible} that it is wheelchair accessible."

    return result


def get_temp(latitude, longitude):
    APIKEY = OPENWEATHERMAP_APIKEY
    country_code = "us"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={APIKEY}&units=imperial"

    response_data = get_json(weather_url)
    temp = response_data["main"]["temp"]
    temp_min = response_data["main"]["temp_min"]
    temp_max = response_data["main"]["temp_max"]

    return temp, temp_min, temp_max


def main():
    """
    You should test all the above functions here
    """
    place_name = "Boston College"
    latitude, longitude = get_lat_long(place_name)
    result = find_stop_near(place_name)
    weather_result = get_temp(latitude, longitude)

    print(f"Latitude: {latitude}, Longitude: {longitude}")
    print(result)
    print(get_temp(latitude, longitude))


if __name__ == "__main__":
    main()
