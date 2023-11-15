import json
import pprint
import urllib.request


# Your API KEYS (you need to use your own keys - very long random characters)

from config import MAPBOX_TOKEN, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """

    # query = "Babson College"
    # query = query.replace(
    #     " ", "%20"
    # )  # In URL encoding, spaces are typically replaced with "%20"
    # url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
        # pprint.pprint(response_data)  # to "pretty print" the response data structure with indentation, so it's easier to visualize.
        return response_data
    # print(response_data['features'][0]['geometry']['address']) #Test


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    query = place_name.replace(" ", "%20")
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    # print(url) 
    #Boston Common: https://api.mapbox.com/geocoding/v5/mapbox.places/Boston%20Common.json?access_token=pk.eyJ1IjoiamVubnlsdW8xIiwiYSI6ImNsb3ExYTJkcTBkaTIyam16d3Q3bmZ6eDYifQ.1TbtY7QfEURsAz5UEzwCkg&types=poi 

    response_data = get_json(url)

    if 'features' in response_data and response_data['features']:
        coordinates = response_data["features"][0]["geometry"]["coordinates"]
        # print(coordinates)
        latitude, longitude = coordinates
        return str(longitude), str(latitude)
    


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    # query = f"{latitude},{longitude}"  
    url=f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    # print(url)
    # https://api-v3.mbta.com/stops?api_key=d2cb2778bea94ada9128d036dbd57114&filter[latitude]=42.3552435&filter[longitude]=-71.065219&sort=distance 
 
    response_data = get_json(url)
    # print(response_data)

    if 'data' in response_data and response_data['data']:
        station_name = response_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1
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
    place_name = "Boston Common"
    latitude, longitude = get_lat_long(place_name)
    print(f'latitude:{latitude}, longitude:{longitude}')

    # station_name, wheelchair_accessible = get_nearest_station(latitude, longitude)
    # print(f'Nearest Station: {station_name}, Wheelchair Accessible: {wheelchair_accessible}')

    station_name, wheelchair_accessible = find_stop_near(place_name)
    print(f'Nearest Station: {station_name}, Wheelchair Accessible: {wheelchair_accessible}')
    


if __name__ == "__main__":
    main()
