import urllib.request
import json
from config import OPENWEATHERMAP_APIKEY
from mbta_helper import get_lat_long

def get_temp(place_name):
    APIKEY = OPENWEATHERMAP_APIKEY 
    lat, lon = get_lat_long(place_name)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}'
    # print(url) #https://api.openweathermap.org/data/2.5/weather?q=Boston,us&APPID=f453898f820799a0556e8a07f017df4c&units=metric 

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        # print(response_text)
        response_data = json.loads(response_text)
        return response_data['main']['temp']


if __name__ == '__main__':
    print(get_temp('Boston Common'))