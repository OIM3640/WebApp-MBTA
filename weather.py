import urllib.request
import json
import pprint



APIKEY = "ea79d934f6dec433380e850232736a5b"
city = 'Wellesley'
country_code = 'us'


# print(url)

def get_temp(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={APIKEY}&units=metric' 
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        # print(response_text)
        response_data = json.loads(response_text)

    return response_data['main']['temp']


if __name__ == "__main__":
    print(get_temp('wellesley'))