import requests

def get_weather_data(city_name):
    api_key = "ae7ff952ade6ca145a23e200804aeb94"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
