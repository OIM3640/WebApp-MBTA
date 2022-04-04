# Your API KEYS (you need to use your own keys - very long random characters)

from urllib import response
import urllib.request
import json
import pprint
from flask import Flask, render_template
from flask import request


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"

MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it


def get_jason(location):
    location=location.replace(" ","%20")
    location=location+",Boston,MA"
    KEY = '6nEiWyNdVHBzlbSojpQr7LtNrf8q7z8N'
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={KEY}&location={location}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    return response_data
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
# get_jason("Boston Common,MA")


def get_lat_long(place_name):
    jsondic=get_jason(place_name)
    lat=jsondic["results"][0]["locations"][0]["latLng"]["lat"]
    lng=jsondic["results"][0]["locations"][0]["latLng"]["lng"]
    city=jsondic["results"][0]["locations"][0]["adminArea5"]
    print(f"{place_name} in Boston, MA's latitude is {lat} and the lontitude is {lng}")
    return((lat,lng))
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
get_lat_long("Boston Common")


def get_nearest_station(place_name):
    lat=str(get_lat_long(place_name)[0])##in North
    lng=str(get_lat_long(place_name)[1]) ## in East
    Key="95406228c02b44e89e44a494c54ae7e9"
    url = f'https://api-v3.mbta.com/stops?api_key={Key}&sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_text=json.loads(response_text)
    # pprint.pprint(response_text)
    return(response_text)

    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """

get_nearest_station("The Boston Common")

def find_stop_near(place_name):
    jasonstops=get_nearest_station(place_name)
    neareststaion=jasonstops["data"][0]["attributes"]["name"]
    ifaccessable=jasonstops["data"][0]["attributes"]["wheelchair_boarding"]
    print(f'the nearest station is {neareststaion}')

    if ifaccessable==0:
        iswheelchair='No wheelchair accessibility information is provided.'
    if ifaccessable==1:
        iswheelchair='The stop is wheelchair is accessable'
    else:
        iswheelchair='This stop is not wheelchair accesible'
    print(iswheelchair)
    return(neareststaion,iswheelchair)
    

    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.

    """

    
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        place_name = request.form['place_name']
        neareststation = find_stop_near(place_name)[0]
        iswheelchair=find_stop_near(place_name)[1]
        return render_template('mbta_station_result.html',place_name=place_name, neareststation=neareststation,iswheelchair=iswheelchair)
    else:
        return render_template("mbta_station.html")



if __name__ =="__main__":
    app.run(debug=True)
    main()
