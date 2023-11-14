import json
import pprint
import urllib.request
from config import MBTA_API_KEY


def MBTA_json(latitude, longitude):
    MBTA_url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"

    with urllib.request.urlopen(MBTA_url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
        #pprint.pprint(response_data)
        #print(MBTA_url)
        return response_data


if __name__ == "__main__":
    pprint.pprint(MBTA_json("42.364506", "-71.038887"))
