# Referenced for request library syntax https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
import requests # I find the requests module is more readable and less complicated than urllib, as I learned from Quiz 4
# from pprint import pprint # not necessary now that the data has been retrieved


# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, OPENWEATHER_TOKEN


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it. I wanted to use it.


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    # Referenced to learn about assigning website data to JSON object https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
    link = requests.get(url)
    link = link.json()
    return link


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_name = str(place_name) # prevents exception related to entering non String
    place = MAPBOX_BASE_URL + place_name + ".json?access_token=" + MAPBOX_TOKEN
    place = get_json(place)
    if place["features"] == []: # this prevents an exception associated with unknown cities/towns (likely because they are made-up/not documented/translated wrong)
        return None # None means that the city/town is not covered by the MAPBOX API
    else:
        latitude = place["features"][0]["center"][1]
        longitude = place["features"][0]["center"][0]
        location = (str(latitude), str(longitude))
        return location


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    station = MBTA_BASE_URL + "?filter[latitude]=" + latitude +"&filter[longitude]=" + longitude + "&sort=distance"
    station = get_json(station)
    if station["data"] == []: # the API does not recognize certain cities/towns, this if statement prevents an exception for out-of-range cities/towns
        return None # None means there are no MBTA stations in that city/town
    else:
        station_name = station["data"][0]["attributes"]["name"]
        wheelchair_accessible = station["data"][0]["attributes"]["wheelchair_boarding"]
        wheelchair_accessible = wheelchair_accessible == 1
        information = (station_name, wheelchair_accessible)
        return information


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    coordinates = get_lat_long(place_name)
    if coordinates == None: # handles exception related to an unknown city/town name
        return None
    else:
        coordinates_latitude = coordinates[0]
        coordinates_longitude = coordinates[1]
        station = get_nearest_station(coordinates_latitude, coordinates_longitude)
        return station


def get_temp(city: str) -> int:
    """
    Returns the temperature of a given town/city
    """
    city = str(city)
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + OPENWEATHER_TOKEN
    link = requests.get(url)
    link = link.json()
    if link["cod"] == "404":
        return None # This will never be displayed on the website, unless OPENWEATHERMAP lacks a location that MBTA has
    else:
        temperature = link["main"]["temp"]
        temperature = int(temperature * 1.8 - 459.67) # people do not reference decimals when discussing tempearture, so converted to int
        return temperature


def main():
    """
    You can test all the functions here
    """
    # location = "Salisbury"
    # coordinates = get_lat_long(location)
    # print(coordinates)

    # coordinates_latitude = coordinates[0]
    # coordinates_longitude = coordinates[1]
    # station = get_nearest_station(coordinates_latitude, coordinates_longitude)
    # print(station)

    print(find_stop_near("Pietradefusi")) # very outside MBTA
    print(find_stop_near("Salisbury")) # outside MBTA
    print(find_stop_near("Boston")) # handicap accessible
    print(find_stop_near("Wellesley")) # handicap inaccessible
    print(find_stop_near("West Roxbury")) # uses a space in the name; does not cause URL issues like anticipated
    print(find_stop_near("Gibberishness")) # location does not exist
    print(find_stop_near(42.0)) # did not enter string

    print(find_stop_near(input("Please enter a city/town to locate a close MBTA station that is or is not handicap accessible >>> ")))

    print(get_temp(42.0))
    print(get_temp('Gibberishness'))
    print(get_temp('Boston'))


if __name__ == '__main__':
    main()
