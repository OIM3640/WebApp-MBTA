# Your API KEYS (you need to use your own keys - very long random characters)
from api_keys import MAPQUEST_API_KEY, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
import urllib.request
import json
import pprint
from flask import Flask, render_template
app = Flask(__name__)

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    
    return response_data

# @app.route("/hello/")
# @app.route("/homepage/<place_name>")

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    http://www.mapquestapi.com/geocoding/v1/address?key=KEY&location=Washington,DC
    """
    get_place_name = place_name.replace(" ", "%20")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={get_place_name}'
    response_data = get_json(url)

    # print(response_data)
    lat = response_data["results"][0]["locations"][0]["latLng"]["lat"]
    lng = response_data["results"][0]["locations"][0]["latLng"]["lng"]

    return lat, lng


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    

    station_info = get_json(url)
    station_name = station_info['data'][0]['attributes']['name']
    wheelchair_available = station_info['data'][0]['attributes']['wheelchair_boarding']
    
    return (station_name, wheelchair_available)
    

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat = get_lat_long(place_name)[0]
    lng = get_lat_long(place_name)[1]

    station = get_nearest_station(lat, lng)
    wh_av = ''
    wheelchair_available = station[1]

    if wheelchair_available == 1:
        wh_av = 'wheelchair available'
    else:
        wh_av = 'wheelchair unavailable'
    return (station[0], wh_av)


def main():
    """
    You can test all the functions here
    """
    print(get_lat_long('Boston'))
    print(get_nearest_station(42.358894, -71.056742))
    print(find_stop_near('Boston'))


if __name__ == '__main__':
    main()
