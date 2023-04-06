import urllib.request
import json
from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from config import APIKEY_Weather

app = Flask(__name__)

country_code = 'us'

def get_weather_conditions(city: str, country_code: str, APIKEY_Weather: str) -> str:
    """
    Given a city and country code, return a string representing the current weather conditions.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY_Weather}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    weather_conditions = response_data["weather"][0]["description"]
    return weather_conditions


def get_local_temperature(city: str, country_code: str, APIKEY_Weather: str) -> float:
    """
    Given a city and country code, return the current temperature in Fahrenheit.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=imperial&appid={APIKEY_Weather}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    temperature = response_data["main"]["temp"]
    return temperature

def recommend_clothes(city: str, country_code: str, APIKEY_Weather: str) -> list:
    temperature = get_local_temperature(city, country_code, APIKEY_Weather)
    weather_conditions = get_weather_conditions(city, country_code, APIKEY_Weather)
    recommendations = []
    if temperature < 40:
        recommendations.append("Remember to bring a jacket!")
    elif temperature > 75:
        recommendations.append("It's time to wear lighter clothes!")
    if "rain" in weather_conditions.lower():
        recommendations.append("Remember to bring an umbrella!")
    elif "snow" in weather_conditions.lower():
        recommendations.append("Recommend staying inside.")
    if "clear" in weather_conditions.lower() or "sunny" in weather_conditions.lower():
        recommendations.append("Remember sunglasses or a hat!")
    return recommendations


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    place_name = request.form.get('place_name')
    try:
        station, is_accessible = find_stop_near(place_name)
        if station is None:
            return render_template('error.html', place_name=place_name)
        recommendations = recommend_clothes(city=place_name, country_code=country_code, APIKEY_Weather=APIKEY_Weather)
        temperature = get_local_temperature(city=place_name, country_code=country_code, APIKEY_Weather=APIKEY_Weather)
        weather_conditions = get_weather_conditions(city=place_name, country_code=country_code, APIKEY_Weather=APIKEY_Weather)
        return render_template('mbta_station.html', place_name=place_name, nearest_station=station, is_accessible=is_accessible, recommendations=recommendations, temperature=temperature, weather_conditions=weather_conditions)
    except:
        return render_template('error.html', place_name=place_name)


if __name__ == '__main__':
    app.run(debug=True)

