from ast import Index
from config import MAPQUEST, MBTA_API
import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(" ", "%20")
    mapquest_url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST}&location={place_name}"
    response = get_json(mapquest_url)
    results = response["results"][0]
    locations = results["locations"]
    for location in locations:
        if location["adminArea3"] == "MA":
            # only return the nearst station's coordinates to the place that is within the state of Massechusettes
            latLng = location["latLng"]
            return (latLng["lat"], latLng["lng"])
        else:
            latLng = location["latLng"]
            return (latLng["lat"], latLng["lng"])


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    mbta_url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API}&sort=distance&sort=wheelchair_boarding&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    response = get_json(mbta_url)
    stations = response["data"]
    nearst_station = stations[0]
    attributes = nearst_station["attributes"]

    station_name = attributes["name"]
    wheelchair_accessible = attributes["wheelchair_boarding"]
    return (station_name, wheelchair_accessible)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    This function might use all the functions above.
    """
    lat_long = get_lat_long(place_name)
    lat = lat_long[0]
    long = lat_long[1]
    # store the latitude and longtitude in lat and long

    try:
        nearst_station = get_nearest_station(lat, long)
    except IndexError as i:
        return "You need to enter a location within the Boston Metro Area!"
        # If the user entered a location that is outside of the area covered bt MBTA

    # Turn number into words
    if nearst_station[1] == 0:
        wheelchair_accesibility = "there is no information regarding wheelchair accessibility"
    elif nearst_station[1] == 1:
        wheelchair_accesibility = "it is wheelchair accessible"
    else:
        wheelchair_accesibility = "it is not wheelchair accessible"

    return f"The closest station to the {place_name} is {nearst_station[0]}, and {wheelchair_accesibility}."


def main():
    """
    You can test all the functions here
    """
    ## test code for location entered outside of MA
    # find_stop_near("empire state building")
    # print(find_stop_near("boston commons"))


if __name__ == "__main__":
    main()
