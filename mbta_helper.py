import json
import pprint
import urllib.request
from datetime import datetime

# urls for mapbox and mbta, along with the API keys
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_API = "0ce5ffa3e30f419193f4cf49a961f979"
MAPBOX_TOKEN = "pk.eyJ1IjoibXJlbjIiLCJhIjoiY2xvcnBvb2xlMHRxbTJqcm5rY2lpZnlqMyJ9.68GvFewXLyOZmEJ2p44mgQ"


# retrieves the json of the requested urls
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
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
    query = place_name.replace(" ", "%20")
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    response_data = get_json(url)
    coordinates = response_data["features"][0]["geometry"]["coordinates"]
    latitude, longitude = coordinates[1], coordinates[0]

    return str(latitude), str(longitude)

OpenWeatherMap_API = '061cc3fc66e13eda49e811f577b68dba'

def get_weather_info(latitude: str, longitude: str) -> dict:
    """
    takes the latitude and longitude to return the weather for that location
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={OpenWeatherMap_API}"
    response_data = get_json(url)

    temp_kelvin = response_data["main"]["temp"]
    # convert kelvin to celsius
    temp_celsius = temp_kelvin - 273.1
    # convert celsius to fahrenheit
    temp_fahrenheit = round(temp_celsius * 9/5) + 32

    weather_info = {
        "temperature": temp_fahrenheit,
        "description": response_data["weather"][0]["description"],
        "humidity": response_data["main"]["humidity"],
        "wind_speed": response_data["wind"]["speed"],
    }
    return weather_info

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"{MBTA_BASE_URL}?sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}&api_key={MBTA_API}"

    response_data = get_json(url)
    station_id = response_data["data"][0]["id"]

    #real-time predictions for station
    predictions_url = f"https://api-v3.mbta.com/predictions?filter[stop]={station_id}&api_key={MBTA_API}"
    predictions_data = get_json(predictions_url)

    #arrival times for the station
    predictions = []
    for prediction in predictions_data["data"]:
        arrival_time = prediction["attributes"]["arrival_time"]
        predictions.append({"arrival_time": arrival_time})

    weather_info = get_weather_info(latitude, longitude)
    return {
        "weather_info": weather_info,
        "station_name": response_data["data"][0]["attributes"]["name"],
        "wheelchair_accessible": response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1,
        "predictions": predictions
    }


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You should test all the above functions here
    """
    place_name = "Harvard University"
    # print(get_lat_long(place_name))
    results = find_stop_near(place_name)
    pprint.pprint(f'The nearest MBTA Stop is {results["station_name"]}')
    pprint.pprint(f'Wheelchair Accessible: {results["wheelchair_accessible"]}')

    predictions = results["predictions"]
    if predictions:
        print("Real-Time Arrival Data:")
        for prediction in predictions:
            arrival_time = prediction.get('arrival_time')  # Use get to handle None
            if arrival_time is not None:
                # Format the date and time
                arrival_time_formatted = datetime.fromisoformat(arrival_time).strftime(" %H:%M (%m-%d-%Y)")
                print(f"Arrival Time is{arrival_time_formatted}")
            else:
                print("Arrival Time: Not available")
        
        weather_info = results.get("weather_info")
        if weather_info:
            print("\nWeather Information")
            print(f"Temperature: {weather_info['temperature']}°F")
            print(f"Description: {weather_info['description']}")
            print(f"Humidity: {weather_info['humidity']}%")
            print(f"Wind Speed: {weather_info['wind_speed']} mph")
        else:
            print("Weather information not available")
    else:
        print("No real-time arrival data available")


if __name__ == "__main__":
    main()
