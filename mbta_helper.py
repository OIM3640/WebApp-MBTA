# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY
import json
import pprint
import urllib.request

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/docs/swagger/swagger.json"


# A little bit of scaffolding if you want to use it
def get_json(query: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """

    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = "pk.eyJ1IjoianNoYW5nb2xkMSIsImEiOiJjbG9xOWl2MHowZHB0MmlvMTBxajMwMHI2In0.w1rTFPExS8lXPFocl185-Q"
    query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    #print(url) # Try this URL in your browser first

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
    query = place_name.replace(' ', '%20')
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'

    # Extracting coordinates from the response
    response_data = get_json(place_name)
    features = response_data.get("features", [])
    coordinates = features[0].get("center", [])
    len(coordinates) == 2
    return tuple(coordinates)

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    mbta_url = f"https://api-v3.mbta.com/stops?apikeysort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    print(mbta_url)


    station_name = ""
    wheelchair_accessible = False

    return station_name, wheelchair_accessible

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    station_name, wheelchair_accessible = get_nearest_station(latitude, longitude)
    return station_name, wheelchair_accessible

 

def main():
    """
    You should test all the above functions here
    """
    # Test get_lat_long function
    place_name = "Atlantic Warehouse"
    latitude, longitude = get_lat_long(place_name)
    print(f"Coordinates for {place_name} are lat:{latitude}, long:{longitude}")

    # Test get_nearest_station function
    station_name, wheelchair_accessible = get_nearest_station(latitude, longitude)
    # print(f"Nearest MBTA Station: {station_name}")
    # print(f"Wheelchair Accessible: {wheelchair_accessible}")

    # Test find_stop_near function
    # stop_name, stop_accessible = find_stop_near(place_name)
    # print(f"Nearest MBTA Stop: {stop_name}")
    # print(f"Wheelchair Accessible: {stop_accessible}")
    #lat, long = get_lat_long(place_name)
    #runner = str(lat) + str(long)
    #print(get_json(runner))

    #https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D=42.364506&filter%5Blongitude%5D=-71.038887



if __name__ == "__main__":
    main()