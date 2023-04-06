# Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it

import urllib.parse
import requests
from pprint import pprint
import random

MAPBOX_API_KEY = "pk.eyJ1IjoiamRpbmcyIiwiYSI6ImNsZnpycTR1aTEwNHozZG1rNzc0eGRsaGUifQ.TXqxolgtqCTPJk3kbB_bQw"
MBTA_API_kEY = "f28ffef47e91409785f061cb7caf1873"


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.
    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    # Send a get request to the specified Url and get JSON reponse
    response = requests.get(url)
    data = response.json()

    # Return the Json reponse as a dictionary
    return data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.
    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    # We set the base URL and our API access token
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = "pk.eyJ1IjoiamRpbmcyIiwiYSI6ImNsZnpycTR1aTEwNHozZG1rNzc0eGRsaGUifQ.TXqxolgtqCTPJk3kbB_bQw"

    # Encode place name as query parameter and build API Url
    query = urllib.parse.quote_plus(place_name)
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"

    # Request access to API and parse the JSON response
    data = get_json(url)

    # If reponse doesn't contain any features, then it returns None, None
    if "features" not in data:
        return None, None

    # Else it extracts the latitute and longitude of the first feature in response
    longitude, latitude = data["features"][0]["center"]

    # Return latitude and longtitude as tuples
    return latitude, longitude


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    # Set up the base api with latitude and longtitude as parameters
    url = f"https://api-v3.mbta.com/stops?sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}&api_key={'f28ffef47e91409785f061cb7caf1873'}"

    # Send a request to the API and parse the JSOn reponse
    data = get_json(url)

    # If there are no stops found, then it will return none for both stop name and wheel chair access
    if not data["data"]:
        return None, None

    # Extract the name and wheelchair accessibility of the nearest stop
    stop_name = data["data"][0]["attributes"]["name"]
    wheelchair_accessible = data["data"][0]["attributes"]["wheelchair_boarding"] == 1

    # Return the stop name and wheelchair accessility as a tuple pair
    return stop_name, wheelchair_accessible


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    This function might use all the functions above.
    """
    # Get the latitude and longitude coordinates for the given place
    latitude, longitude = get_lat_long(place_name)

    # If no coordinates were found, return None
    if latitude is None or longitude is None:
        return None

    # Find the nearest MBTA station to the given coordinates
    station_name, wheelchair_accessible = get_nearest_station(latitude, longitude)

    # return tuple station name as string and wheel assessible as boolean
    return station_name, wheelchair_accessible


def get_weather(latitude: float, longitude: float) -> tuple[float, str]:
    """
    This function takes in parameters latitude and longtitude and outputs temperature(float) and weather descrption(string)
    """
    # Replace YOUR_API_KEY with your actual API key from OpenWeatherMap
    API_KEY = "ae7ff952ade6ca145a23e200804aeb94"

    # Make a request to the OpenWeatherMap API to get the weather for the given location
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
    response = requests.get(url)

    #  HTTP status code, it means "OK"
    if response.status_code == 200:
        # Parse the response to get the temperature and weather description
        data = response.json()

        # convert temperature from Kelvin to celcius
        temperature = round((data["main"]["temp"] - 273.15))

        # get the weather description
        weather_description = data["weather"][0]["description"]

        # return a tuple with temperature as float and weather description as str
        return temperature, weather_description
    else:
        # If status is not "OK", then it will return None, None for both variables
        return None, None


def get_event(latitude, longitude):
    """
    This function takes in Lat and Long parameter and return the name and date of a random nearby music event within 5 miles.
    """
    #  Set the base URL for ticketmaster
    url = "https://app.ticketmaster.com/discovery/v2/events.json"

    # Encode the following as a query parameter and build the API URL
    params = {
        "apikey": "9L0f7AhrIsAgxEqLR9ogxZ4c6NOGUptl",
        "latlong": str(latitude) + "," + str(longitude),
        "keyword": "music",
        "radius": "5",
        "unit": "miles",
    }

    # Request the url along with its parameters
    response = requests.get(url, params=params)

    # Parse the JSON response
    data = response.json()

    # If there are events within the given parameter, the following code executes
    if "_embedded" in data:
        # Extract the event data from the response
        events = data["_embedded"]["events"]

        # A random event is assigned to the random event variable from events dictionary
        random_event = random.choice(events)

        # Return the event name and event date as string tuples
        return random_event["name"], random_event["dates"]["start"]["localDate"]
    else:
        # Return none if there are no event found
        return None


def main():
    """
    You can test all the functions here
    """
    place_name = "Boston College"
    station_name, wheelchair_accessible = find_stop_near(place_name)
    if station_name is None:
        print(f"No MBTA stop was found near {place_name}.")
    else:
        print(f"The nearest MBTA stop to {place_name} is {station_name}.")
        print(f"It is{' ' if wheelchair_accessible else ' not '}wheelchair accessible.")
    print(get_event(latitude=42.334515, longitude=-71.168648))


if __name__ == "__main__":
    main()
