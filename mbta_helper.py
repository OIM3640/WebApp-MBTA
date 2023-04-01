import requests
import json

# Your API KEYS (you need to use your own keys - very long random characters)

MBTA_KEY = "f2e4dbfbd54940b7b181479f7aa389b4"

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"
    key = {
        "access_token": "pk.eyJ1Ijoic2xpOSIsImEiOiJjbGZ2cWlueDYwMDg5M2RvZGp4bGt1dDZ4In0.OhZHNyEJGKdMYpuhOkeMNQ"
    }
    response = requests.get(url, params=key)
    response_json = response.json()
    features = response_json.get("features")
    if features and len(features) > 0:
        first_feature = features[0]
        geometry = first_feature.get("geometry")
        if geometry:
            latitude = geometry.get("coordinates")[1]
            longitude = geometry.get("coordinates")[0]
            return latitude, longitude
    return None, None


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"https://api-v3.mbta.com/stops"
    coords = {
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "sort": "distance",
        "page[limit]": 1,
    }
    response=requests.get(url,params=coords)
    response_json=response.json()
    data=response_json.get("data")
    if data and len(data)>0:
        stop=data[0]
        attributes=stop.get("attributes")
        name=attributes.get("name")
        wheelchair=attributes.get("wheelchair_boarding")
        if wheelchair is not None:
            wheelchair_accessible= True if wheelchair == 1 else False
        else:
            wheelchair_accessible = None
        return name, wheelchair_accessible
    return None, None



def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude=get_lat_long(place_name)[0]
    longitude=get_lat_long(place_name)[1]
    return get_nearest_station(latitude,longitude)


def main():
    """
    You can test all the functions here
    """
    commons="Boston Commons"
    # commons_coords=get_lat_long(commons)
    # print(commons_coords)
    # lat = commons_coords[0]
    # lng = commons_coords[1]
    # print(get_nearest_station(lat, lng))

    print(find_stop_near(commons))


if __name__ == "__main__":
    main()
