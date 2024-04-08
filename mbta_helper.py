import json
import pprint
import urllib.request
import urllib.parse
import requests

# Your API KEYS (you need to use your own keys - very long random characters)
from config1 import MAPBOX_TOKEN, MBTA_API_KEY


# query = 'Babson College'
# query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20". You can also use urllib.parse.quote function.
# print(url) # Try this URL in your browser first
# with urllib.request.urlopen(url) as f:
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#     pprint.pprint(response_data)

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# A little bit of scaffolding if you want to use itV


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
        return response_data


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = urllib.parse.quote(place_name)
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    response_data = get_json(url)

    longtitude, latitude = response_data["features"][0]["center"]
    return str(latitude), str(longtitude)
    # coordinates = response_data["features"][0]["geometry"]["coordinates"]
    # return tuple(coordinates)


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    mbta_api_url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    response_data = requests.get(mbta_api_url).json()
    # this url works in chrome: https://api-v3.mbta.com/stops?filter[latitude]={42.2981925}&filter[longitude]={-71.263598}
    # pprint.pprint(response_data), empty dataset
    if len(response_data["data"]) != 0:
        stops = response_data["data"][0]
        station_name = stops["attributes"]["name"]
        wheelchair_accessible = stops["attributes"]["wheelchair_boarding"]
        if wheelchair_accessible == 1:
            wheelchair_accessible = True 
        else: 
            wheelchair_accessible = False
            # print("Station name:", station_name)  # Print the station name
            # print("Wheelchair accessible:", wheelchair_accessible)
        return station_name ,wheelchair_accessible
    else:
        return "No station has been found", False
        
    


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat, lng = get_lat_lng(place_name)

    station_name, wheelchair_accessible = get_nearest_station(lat,lng)
    wheelchair_accessible = wheelchair_accessible == 1
    return station_name, wheelchair_accessible
    
    


def main():
    """
    You should test all the above functions here
    """
    print(get_lat_lng("Boston College"))
    print(find_stop_near("Boston University"))
    print(get_nearest_station(42.3358655,-71.1694295))


if __name__ == "__main__":
    main()
