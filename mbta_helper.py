# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY, WEATHER_API_KEY

import pprint
import json
import urllib.request

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
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)

        return response_data

def get_url(place_name):
    """
    This function takes an address and reutrns a URL
    """
    place_name = place_name.replace(' ', '%20')# + ",Boston,MA"
    url=f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi' 
    return url           

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    # print(url) # Try this URL in your browser first
    url = get_url(place_name)
    response_data = get_json(url) #format properly
    longitude, latitude = response_data["features"][0]["center"]  # coordinates are longitude then latitude
    return latitude, longitude

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    nearest_station = MBTA_BASE_URL + "?filter[latitude]=" + str(latitude) +"&filter[longitude]=" + str(longitude) + "&sort=distance"
    nearest_station_data = get_json(nearest_station)
    if nearest_station_data["data"] == []: #stops exception for out-of-range cities
        #answer = 'There are no stations near this location'
        answer = None
        if answer == None:
            print('There are no stations near this location')
        return answer
    else:
        nearest_station_name = nearest_station_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = nearest_station_data["data"][0]["attributes"]["wheelchair_boarding"]
        if wheelchair_accessible == 1 or wheelchair_accessible == 2:
            wheelchair_accessible = 'This station is wheelchair accessible'
        else:
            wheelchair_accessible = 'This station is not wheelchair accessible'
        information = (nearest_station_name, wheelchair_accessible)
        return information

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat_long = get_lat_long(place_name)
    if lat_long == None: #handles exceptions again
        return None
    else:
        latitude = lat_long[0] #gets 1st object for latutude
        longitude = lat_long[1]
        station = get_nearest_station(latitude, longitude)
        return station

def get_temp(city):
    APIKEY = WEATHER_API_KEY
    country_code = 'us'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}&units=metric'

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        # print(response_text)
        response_data = json.loads(response_text)
        temp_in_farenheit = ((response_data['main']['temp'])*(9/5)) + 32
        temp_feel = ((response_data['main']['feels_like'])*(9/5))+32
        return temp_in_farenheit, temp_feel

def main():
    """
    You should test all the above functions here
    """
    "Test get_json"
    place_name = 'Boston Common'
    url = get_url(place_name)
    print(url)

    "Get lattitude and longitude"
    lat_long = get_lat_long(place_name)
    print(lat_long)
    print(type(lat_long))

    "Nearest Station + wheelchair access"
    latitude = lat_long[0] #gets 1st object for latutude
    longitude = lat_long[1]
    station = get_nearest_station(latitude, longitude)
    print(station)

    "nearest station, using input"
    print(find_stop_near(input("Please enter a city to find a close MBTA station ")))

    "Get Temp"
    temp, temp_feel = get_temp('boston')
    print(f' the temperature in Boston is {temp:.2f} degrees, but it feels like it is {temp_feel:.2f} degrees')

if __name__ == '__main__':
    main()
