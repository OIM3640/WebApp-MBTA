import json
import urllib.request
from urllib.error import URLError, HTTPError
from config import MAPBOX_TOKEN, MBTA_API_KEY, WEATHER_API

# Base URLS for Mapbox, MBTA, and OpenWeatherMap APIs
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_json(url: str) -> dict:
    """
    Function to retrieve JSON data from a given URL
    Input: URL
    Returns: Dict of JSON data
    """
    try:
        with urllib.request.urlopen(url) as f:
            response = f.read().decode('utf-8')
            response_data = json.loads(response) # Data from URL page
            return response_data
    except (HTTPError, URLError) as e: # Deals with errors
        print(f"Error getting data from {url}: {e}")
        return{}
    

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Function to get latitude and longitude from a place name or address using Mapbox API
    Takes: Place name or address
    Returns: Latitude, Longitude
    """
    place_name = place_name.replace(" ", "%20") # replaces spaces with url-formatted space character
    url = f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi'
    response_data = get_json(url)
    longitude, latitude = response_data["features"][0]["center"] # locations in dict
    return latitude, longitude

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Function to get the nearest MBTA station & wheelchair accesisibility information based on latitude and longitude
    Takes: Latitude & Longitude
    Returns: Name of station and accessibility status
    """
    url = f"{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}" # filters using long & lat then sorts by nearest distance to that location
    response_data = get_json(url)

    station_name = response_data["data"][0]["attributes"]["name"]
    wheelchair_accessibility = response_data["data"][0]["attributes"]["wheelchair_boarding"]

    return station_name, wheelchair_accessibility

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Function to find the nearest stop and provide accesibility message
    Takes: Place name or address
    Returns: Nearest station and accesibility message
    """
    longitude, latitude = get_lat_long(place_name)
    name, accessible = get_nearest_station(longitude, latitude)

    if accessible == 0: # Writes a message about accessibility
        wheelchair_message = "This is no information about wheelchair accessibility."
    elif accessible == 1:
        wheelchair_message = "This stop is wheelchair accessible."
    elif accessible == 2:
        wheelchair_message = "This stop is not wheelchair accessible."
    
    result = f"The nearest MBTA stop is {name}. {wheelchair_message}"
    return result, accessible

def get_weather():
    """
    Returns weather in Farenheit for Boston, MA
    """
    city = "Boston"
    country_code = 'us'

    url = f"{WEATHER_BASE_URL}?q={city},{country_code}&APPID={WEATHER_API}&units=imperial"
    response_data = get_json(url)
    
    temp = response_data["main"]["temp"] # temperature in F
    desc = response_data["weather"][0]["description"] # description of weather according to API

    return {"large": f"{temp}°F", "small": f"Weather: {desc}"} # Dict so it's easier to format in Flask


def main():
    """
    Function Tester
    """
    place_name = input("Current Location: ")
    print(find_stop_near(place_name))
    print(get_weather())
if __name__ == '__main__':
    main()
