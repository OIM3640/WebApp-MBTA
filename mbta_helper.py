# Your API KEYS (you need to use your own keys - very long random characters)
import urllib.request
import json
from pprint import pprint
from config import MAPBOX_TOKEN, MBTA_API_KEY, WEATHER_KEY


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
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(" ", "%20") #fill empty space
    url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}"
    response_data = get_json(url)
    longitude, latitude = response_data["features"][0]["center"]
    #Round coordinates to appropriate length
    latitude = round(latitude, 3)
    longitude = round(longitude, 3)
    return latitude, longitude


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    response_data = get_json(url)
    # response_data['data']:
    try:
        stop = response_data['data'][0]
        # Gets station name
        station = stop['attributes']['name']
        # Gets BOOL for station's accesibility 
        wheelchair = stop['attributes']['wheelchair_boarding'] == 1
        return station, wheelchair
    except:
        return None, None



def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude) 

def get_weather(place_name:str):
    """
    Given a place name or address, returns the current weather and temperature.
    """
    place_name = place_name.replace(" ", "%20")
    latitude, longitude = get_lat_long(place_name)
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={WEATHER_KEY}&units=metric"
    weather_data = get_json(url)
    # Gets current temperature (in farenheit) and weather conditions
    temperature = weather_data["main"]["temp"]
    temperature_f= float(temperature *(9/5))+32
    weather = weather_data["weather"][0]["main"]
    return weather, temperature_f



def main():
    """
    You should test all the above functions here
    """
    location = "Babson College"
    pprint(location)
    pprint(get_lat_long(location))
    pprint(find_stop_near(location))
    pprint(get_weather(location))


if __name__ == '__main__':
    main()
