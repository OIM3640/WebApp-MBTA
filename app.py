from flask import Flask, render_template, request, redirect, url_for
from config import MAPBOX_TOKEN, MBTA_API_KEY, WEATHER_APIKEY, TICKET_KEY
import urllib.request
import json
import pprint

app = Flask(__name__)

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/nearest_station', methods=['POST'])
def nearest_station():
    place_name = request.form['place_name']
    longitude, latititude = get_lat_long(place_name)
    response_data = get_temperature(city='boston')
    station_name, wheelchair_accessible = get_nearest_station(longitude, latititude)
    return render_template('nearest_mbta.html', place_name = place_name, station_name = station_name, wheelchair_accessible=wheelchair_accessible, response_data= response_data)
def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20')
    url =f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi'

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)

    longitude, latitude = response_data['features'][0]['center']
    return latitude,longitude 

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    mbta_url = f"{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}"

    with urllib.request.urlopen(mbta_url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint(response_data)

        station_name = response_data['data'][0]['attributes']['name']

        wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding']
        return station_name, wheelchair_accessible

def get_temperature(city):
    """
    
    """
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={WEATHER_APIKEY}&units=metric'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    
    return response_data['main']['temp']

if __name__ == '__main__':
    app.run(debug=True)
