import urllib.request
import json
import pprint
from config import OPENWEATHERMAP_APIKEY


def get_temp(place: str) -> float:
    """
    return the current temperature of a given city
    """
    place = place.replace(' ', '%20')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={place},us&APPID={OPENWEATHERMAP_APIKEY}&units=metric'
    print(url)

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        # print(response_text)
        response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    return response_data['main']['temp']

def main ():
    print(get_temp('wellesley'))

if __name__ == "__main__":
    main()