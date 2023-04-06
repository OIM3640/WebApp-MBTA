# Your API KEYS (you need to use your own keys - very long random characters)
import json
import requests
import pathlib, os

confifDir = pathlib.Path(__file__).parent
with open(os.path.join(confifDir, "config.json")) as configFile:
    config = json.load(configFile)


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it


def get_json(url: str) -> dict:
    response = requests.get(url=url)
    content = response.json
    return content
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
   


def get_lat_long(place_name: str) -> tuple[str, str]:
    place_name = place_name.replace(" ","%20")
    url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={config['MAPBOX_TOKEN']}"
    content = get_json(url=url)
    long, lat = content['features'][0]['center']
    return long, lat
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """



def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    url = f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    content = get_json(url=url)
    try:
        attributes = content ["data"][0]["attributes"]
    except:
        return "Not Found", None
    is_wheelchair_accessible = attributes["wheelchair_boarding"]
    name = attributes["name"]
    return name, is_wheelchair_accessible
    

    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """



def find_stop_near(place_name: str) -> tuple[str, bool]:
    long, lat = get_lat_long(place_name)
    name, is_wheelchair_accessible = get_nearest_station(long, lat)
    status = 200
    if is_wheelchair_accessible == 0:
        wheelchair_message = "There is no information about wheelchair accessibility."
    elif is_wheelchair_accessible == 1:
        wheelchair_message = "This station is wheelchair accessible."
    elif is_wheelchair_accessible == 2:
        wheelchair_message = "This station is not wheelchair accessible."
    else:
        wheelchair_message = ""
        status = 400

    result = f"The nearest MBTA stop is {name}. {wheelchair_message}"
    return result, status
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """



def main():
    place_name = input("Enter the place where you are:")
    print(find_stop_near(place_name=place_name  ))
    """
    You can test all the functions here
    """
    


if __name__ == '__main__':
    main()
