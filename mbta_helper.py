# Your API KEYS (you need to use your own keys - very long random characters)
from config import (
    MAPBOX_TOKEN,
    MBTA_API_KEY,
)  # importing API keys from config for security reasons

# Start of 1.2 pasted from the instructions
import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
query = "Babson College"
query = query.replace(
    " ", "%20"
)  # In URL encoding, spaces are typically replaced with "%20"
url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
print(url)  # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    pprint.pprint(response_data)

print(response_data["features"][0]["properties"]["address"])  # prints 231 Forest St


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_json(url: str) -> dict:
    """
    Given a URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as response:  # open URL
        return json.loads(
            response.read().decode("utf-8")
        )  # read, decode, and parse the JSON response (converting the JSON formatted string received from the web API into Python data ). utf-8 is capable of encoding all possible characters.


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = urllib.parse.quote(
        place_name
    )  # Chat GPT suggested to add this line just in case the input contains any special characters like "!"
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"

    response_data = get_json(url)  # get the JSON response data
    if response_data and response_data.get(
        "features"
    ):  # checks if response_data contains the features key
        longitude, latitude = response_data["features"][0][
            "center"
        ]  # extract coordinates using center, 0 is selecting the first result
        return latitude, longitude  # return latitude and longitude
    else:
        print("No coordinates found")


# The get_lat_long function directly feeds into the find_stop_near function by providing essential data. It takes a place name as input, grabs the latitude and longitude using the Mapbox Geocoding API, and feeds the coordinates to find_stop_near. find_stop_near uses these coordinates to determine the nearest MBTA station and if its wheelchair accessible.


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """

    latitude, longitude = get_lat_long(
        place_name
    )  # get the latitude and longitude for the place name
    if latitude is None or longitude is None:
        return None, None  # returns none if coordinates are not found

    url = (
        ""
        f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}"
    )

    response_data = get_json(url)  # getting json response data from the url
    if response_data and response_data.get(
        "data"
    ):  # ensures that response_data is valid
        nearest_stop = response_data["data"][
            0
        ]  # get the first element of the data, this represents nearest stop, it uses [0] because the first item represents its the nearest one
        stop_name = nearest_stop["attributes"][
            "name"
        ]  # getting the name of nearest stop
        wheelchair_accessible = (
            nearest_stop["attributes"]["wheelchair_boarding"] == 1
        )  # checks if its wheelchair accessible, if its a 1 it means that it's wheelchair accesible, if it's a 2 its not wheelchair accessible
        return stop_name, wheelchair_accessible
    else:
        print("Not found")
        return None, None


# def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
#     """
#     Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

#     See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
#     """
#     pass


def main():
    """
    Testing all the above functions here
    """


# Calling the get_lat_long function
place_name = "Boston Commons"  # example place name

latitude, longitude = get_lat_long(place_name)  # call the function with the place name

# check if coordinates were found and print them
if latitude and longitude:  # checks if lat and long are true values
    print(
        f"The coordinates of {place_name}: Latitude {latitude}, Longitude {longitude}"
    )
else:
    print(f"Could not find the coordinates for {place_name}")


# calling find_stop_near function
stop_name, wheelchair_accessible = find_stop_near(place_name)

if stop_name:
    print(f"The nearest MBTA Stop to {place_name} is {stop_name}")
    if wheelchair_accessible:
        accessibility_status = "This station is wheelchair accessible"
    else:
        accessibility_status = "This station is not wheelchair accessible"
    print(f"{accessibility_status}")
else:
    print(f"Could not find the nearest MBTA station for {place_name}")


if __name__ == "__main__":
    main()
