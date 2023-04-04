import urllib.request
import json
from config import OPENAIAPIKEY

def get_temp(city):
    """
    """
    # city = city.replace(" ", "%20")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={OPENAIAPIKEY}&units=metric'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    return response_data["main"]["temp"]