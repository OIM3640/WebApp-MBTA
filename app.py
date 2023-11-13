from flask import Flask, render_template, request
from mbta_helper.mbta_helper import find_stop_near, get_lat_long
from config import OPENWEATHERMAP_API_KEY
import requests
import urllib.parse

app = Flask(__name__)

def get_weather_data(lat, lon):
    weather_api_key = OPENWEATHERMAP_API_KEY
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=imperial"
    weather_response = requests.get(weather_url)
    if weather_response.status_code == 200:
        return weather_response.json()
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nearest_station', methods=['POST'])
def nearest_station():
    stop_name = "Unknown"
    accessible = "Unknown"
    accessibility_status = "Unknown"
    google_maps_url = "#"
    temperature = None
    weather_description = "Weather information is currently unavailable."

    location = request.form['location']
    try:
        stop_name, accessible_flag = find_stop_near(location)
        latitude, longitude = get_lat_long(location)
        google_maps_query = urllib.parse.quote_plus(f"{stop_name} Station Boston MA")
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={google_maps_query}"
        accessibility_status = "Wheelchair Accessible" if accessible_flag else "Not Wheelchair Accessible"

        weather_data = get_weather_data(latitude, longitude)
        if weather_data:
            temperature = weather_data['main']['temp']
            weather_description = weather_data['weather'][0]['description']

    except Exception as e:
        print(f"An error occurred: {e}")
    # for this section I asked StackOverFlow 
    # how I could have multiple things pop up
    # in a line on my web application
    return render_template('results.html', 
                           location=location, 
                           stop_name=stop_name, 
                           accessible=accessible, 
                           accessibility_status=accessibility_status, 
                           google_maps_url=google_maps_url,
                           temperature=temperature, 
                           weather_description=weather_description)

if __name__ == '__main__':
    app.run(debug=True)
