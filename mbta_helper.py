# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY, OPEN_WEATHER_APIKEY
import requests
import json
import pprint
import urllib.request


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

query = "Boston College"
query = query.replace(" ", "%20")
# In URL encoding, spaces are typically replaced with "%20". You can also use urllib.parse.quote function.
url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
# print(url)  # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
    return response_data


# pprint.pprint(get_json(url))


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = place_name.replace(" ", "%20")
    query = query.replace(" ", "%20")
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        longitude, latitude = data["features"][0]["center"]
        return str(latitude), str(longitude)
    else:
        # Handle errors
        return "Error", "Error"


# lat, lng = get_lat_lng("Babson College")
# print(lat, lng)
# lat, lng = get_lat_lng("Boston College")
# print(lat, lng)


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"

    response_data = get_json(url)

    if len(response_data["data"]) == 0:
        return "Could not find a stop nearby", False
    else:
        name = response_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = response_data["data"][0]["attributes"][
            "wheelchair_boarding"
        ]
        wheelchair_accessible = bool(wheelchair_accessible)
        return (name, wheelchair_accessible)


# print(get_nearest_station(lat, lng))
# print(get_nearest_station(42.3358655, -71.1694295))


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat, lng = get_lat_lng(place_name)
    if lat == "Error" or lng == "Error":
        return "Error in getting the coordinates", False

    station_name, wheelchair_accessible = get_nearest_station(lat, lng)
    wheelchair_accessible = bool(wheelchair_accessible)
    return station_name, wheelchair_accessible


# Additional APIs
def real_time_nearest_station(place_name: str) -> tuple[str, bool]:
    """
    Given the place name, return the nearest MBTA stop and whether it is wheelchair accessible as well as the real-time data for that stop.
    """
    lat, lng = get_lat_lng(place_name)
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&sort=distance"
    response_data = get_json(url)

    if len(response_data["data"]) == 0:
        return "Could not find a stop nearby", False
    else:
        name = response_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = response_data["data"][0]["attributes"][
            "wheelchair_boarding"
        ]
        wheelchair_accessible = bool(wheelchair_accessible)
        stop_id = response_data["data"][0]["id"]
        url_stop = f"https://api-v3.mbta.com/schedules?api_key={MBTA_API_KEY}&filter[stop]={stop_id}"

        real_time_nearest_station_data = get_json(url_stop)
        # pprint.pprint(real_time_nearest_station_data)
        arrival_time = real_time_nearest_station_data["data"][0]["attributes"][
            "arrival_time"
        ]
        departure_time = real_time_nearest_station_data["data"][0]["attributes"][
            "departure_time"
        ]
        return (name, wheelchair_accessible, arrival_time, departure_time)


# print(real_time_nearest_station("Boston University"))


def get_city_name(place_name: str) -> str:
    """
    Given a place name or address, return the city name of the given place.
    """
    lat, lng = get_lat_lng(place_name)
    if lat == "Error" or lng == "Error":
        return "Error in getting the coordinates"

    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&sort=distance"
    placedata = get_json(url)
    if not placedata or "data" not in placedata or not placedata["data"]:
        return "No data found"

    return placedata["data"][0]["attributes"]["municipality"]


# print(get_city_name("Boston College"))


def get_city_weather(place_name):
    """
    Given a place name or address, return the current temperature in Fahreneit , main weather condition, and a brief description of the weather for the city.
    """
    city = get_city_name(place_name)
    country_code = "us"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={OPEN_WEATHER_APIKEY}&units=imperial"

    try:
        with urllib.request.urlopen(url) as f:
            response_text = f.read().decode("utf-8")
            response_data = json.loads(response_text)

        weather_data = {
            "temperature": response_data["main"]["temp"],
            "condition": response_data["weather"][0]["main"],
            "description": response_data["weather"][0]["description"],
        }
        return weather_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "Failed to retrieve weather data"}


weather_info = get_city_weather("Boston College")
print(weather_info)


def nearby_events(place_name):
    """
    Retrieves a list of nearby events based on the given place name.
    """


def main():
    """
    You should test all the above functions here
    """
    print("Coordinates for Boston College:")
    print(get_lat_lng("Boston College"))
    print("Coordinates for Boston University:")
    print(get_lat_lng("Boston University"))
    print("Nearest MBTA station for Boston College:")
    print(get_nearest_station(42.3358655, -71.1694295))
    print(find_stop_near("Boston College"))
    print(find_stop_near("Boston University"))
    print(real_time_nearest_station("Boston College"))
    print(real_time_nearest_station("Boston University"))
    print(real_time_nearest_station("Massachusetts Institute of Technology"))


if __name__ == "__main__":
    main()
