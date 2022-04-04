import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = "nhtAFe6Ab0tkNfk5BAvA4M6Q4Ak1QAJY"

MBTA_API_KEY = "ec26d4a19d1e4f148bd5ebec7e08a04e"


url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College"
print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode("utf-8")
response_data = json.loads(response_text)
# pprint(response_data)

print(response_data["results"][0]["locations"][0]["postalCode"])
