from flask import Flask, request, render_template
import json
import urllib.request
from config import MAPBOX_TOKEN, MBTA_API_KEY, OPENWEATHER_API, EVENTBRITE_TOKEN


MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
EVENTBRITE_BASE_URL = 'https://www.eventbriteapi.com/v3/'
OPENWEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        place_name = request.form.get('place')
        if place_name:
            lat, long = get_lat_long(place_name)
            station_name, wheelchair_accessible = find_stop_near(place_name)
            weather_data = get_weather_data(lat, long)
            weather_info = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            # eventbrite_events = get_eventbrite_events(lat, long)
            return f"Nearest MBTA station to {place_name} is {station_name}, Wheelchair accessible: {'Yes' if wheelchair_accessible else 'No'}. Weather near {place_name} is {weather_info}, Temperature: {temp} Kelvins."
            # Events near you: {eventbrite_events}
        else:
            return "Please provide a place name."
    return render_template('index.html')


@app.route('/nearest_mbta')
def nearest_mbta():
    place_name = request.form.get('place')
    if place_name:
        lat, long = get_lat_long(place_name)
        weather_data = get_weather_data(lat, long)
        station_name, wheelchair_accessible = get_nearest_station(lat, long)
        result = {
            'station_name': station_name,
            'wheelchair_accessible': 'Yes' if wheelchair_accessible else 'No', 'weather_data': weather_data
        }
        return result
    else:
        return "Please provide a place name."


def get_json(url: str) -> dict:
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
    return json.loads(response_text)


def get_lat_long(place_name: str) -> tuple[str, str]:
    query = place_name.replace(' ', '%20')
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}'
    response = get_json(url)
    coordinates = response['features'][0]['geometry']['coordinates']
    return str(coordinates[1]), str(coordinates[0])


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    response = get_json(url)
    station = response['data'][0]
    return station['attributes']['name'], station['attributes']['wheelchair_boarding'] == 1


def find_stop_near(place_name: str) -> tuple[str, bool]:
    lat, long = get_lat_long(place_name)
    return get_nearest_station(lat, long)


def get_weather_data(latitude: str, longitude: str) -> dict:
    url = f"{OPENWEATHER_BASE_URL}?lat={latitude}&lon={longitude}&appid={OPENWEATHER_API}"
    return get_json(url)

# def get_eventbrite_events(latitude: str, longitude: str) -> dict:
#     url = f"{EVENTBRITE_BASE_URL}/events/search/?token={EVENTBRITE_TOKEN}&location.latitude={latitude}&location.longitude={longitude}"
#     return get_json(url)


if __name__ == '__main__':
    app.run(debug=True)
