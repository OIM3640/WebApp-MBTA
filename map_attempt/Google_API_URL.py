"""
Replace Google_API_URL.py in the mbta_station_map.html with the printed URL.
"""

from config import GOOGLE_MAPS_API

Google_API_URL=f"https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API}&callback=initMap"
print(Google_API_URL)