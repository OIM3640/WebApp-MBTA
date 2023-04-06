import json
import requests
import pathlib, os

configDir = pathlib.Path(__file__).parent
with open(os.path.join(configDir, "config.json")) as configFile:
    config = json.load(configFile)

def get_json(url: str) -> dict:
    response = requests.get(url=url)
    content = response.json()
    return content 

def get_weather_report(latitude: str, longitude: str) -> tuple:
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={config['WEATHER_KEY']}"
    content = get_json(url=url)
    condition = content["weather"][0]["main"]
    temp = f'{content["main"]["temp"]} {chr(176)}F'
    return condition, temp 

def main(): 
    print(get_weather_report(42.3456, -72.9420))

if __name__ == '__main__':
    main()