Luke Pata

Project Overview:

For this project I used 3 different APIs. One was for location, another was for MBTA stations, and the last one was for weather which was used in class. The web page will ask the user for their current location and then it will give them the closest station. This station is any MBTA station (Bus, Train, or other). It will also tell the user whether or not it is wheelchair accessible (or if it doesn't know, which is the case for a couple locations). Then lastly, it will say the current temperature out. To spoil it, if the user puts in Fenway Park then there is a hidden message that also appears for the user. There is also a fail safe if a location is invalid which will tell the user that there was a problem and that they need to try a differnet location. 

Reflection:

Process- This code was actually eaier to me than past assignments surprisingly. I foudn all of the python work to go well and going through APIs was a lot easier than compared to when we first started. The only prblem that I had was that I orignally amde my code work perfectly for just python without considering the web part of the project. So I went back and reverse engineered my code so that it works with html. This is why some of my original python code is not as pretty as it was in previous pushes. Overall I thought that project was good and really enjoyable to do. 

Team Work Division- I worked alone on this assignment and enjoyed that. It would have been interesting to have a differnet perspective as well, but I think I understand my code a lot better now that I have full responsiblity over it. 

Learning Perspective- I think going forward I would explore more with what I could do. I like the idea of having more hidden messages according to differnet locations. Also possible finding a way to incorporate the weather API more (mainly through fun messages that pop up based on the weather: Ex. "Bring a coat" or "Don't forget the umbrella"). Chat GPT helped with little process that I sometimes needed exmaplined from class when I was having mental blocks. Some examples of my conversations are listed below. 


______________________________________________________________________

Could you debug the code that I put next
Of course! Please provide the code so I can take a look at it.




Luke Pata
def get_nearest_station() -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    lat_long_tuple = get_lat_long()
    latitude = str(lat_long_tuple[0])
    longitude = str(lat_long_tuple[1])
    url=f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5B{latitude}%5D=-71.064822&filter%5B{longitude}%5D=42.354107'
    # print(url)
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        pprint(response_data)
        # return response_data
I see that the function get_nearest_station() relies on the function get_lat_long() to retrieve the latitude and longitude coordinates of a location. However, the code for get_lat_long() is not shown, so I cannot verify its correctness.

Additionally, the function is missing the import statements for the urllib and json modules. Please make sure that the following import statements are included at the beginning of the code:

javascript
Copy code
import urllib.request
import json
from pprint import pprint
Also, MBTA_API_KEY is not defined in the code. Please make sure that it is defined as a string variable before using it in the URL.

Finally, the response_data variable is uncommented, which means that the function is not returning the desired output. Please uncomment the return statement to return the response_data as a tuple of (station_name, wheelchair_accessible).

Here is the updated code:

python
Copy code
import urllib.request
import json
from pprint import pprint

def get_nearest_station() -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    lat_long_tuple = get_lat_long()
    latitude = str(lat_long_tuple[0])
    longitude = str(lat_long_tuple[1])
    url=f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5B{latitude}%5D=-71.064822&filter%5B{longitude}%5D=42.354107'
    # print(url)
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        pprint(response_data)
        return (response_data['data'][0]['attributes']['name'], response_data['data'][0]['attributes']['wheelchair_boarding'] != 'NO_INFORMATION')
Note that the current implementation of get_nearest_station() assumes that the MBTA API returns at least one station in the response. If the API response is empty, this function will raise a KeyError. You may want to add error handling to the function to handle this case appropriately.






I am going to put json code next and can you tell me how I select the value for 'latitude' in python
Sure! To select the value for the 'latitude' key from the JSON data in Python, you can use the json.loads() function from the json module to parse the JSON data into a Python dictionary, and then access the value using the key 'latitude'.

Here's an example:




Luke Pata
{'attributes': {'address': 'Washington St and E Berkeley St, Boston, '
                                     'MA',
                          'at_street': 'East Berkeley Street',
                          'description': 'Washington St @ E Berkeley St - '
                                         'Silver Line - South Station/Downtown '
                                         'Crossing',
                          'latitude': 42.344189,
                          'location_type': 0,
                          'longitude': -71.065726,
                          'municipality': 'Boston',
                          'name': 'Washington St @ E Berkeley St',
                          'on_street': 'Washington Street',
                          'platform_code': None,
                          'platform_name': 'South Station/Downtown Crossing',
                          'vehicle_type': 3,
                          'wheelchair_boarding': 1}
To select the value for the 'latitude' key from the JSON data you provided, you can do the following:

makefile
Copy code
import json

# Example JSON data
json_data = '{"attributes": {"address": "Washington St and E Berkeley St, Boston, MA","at_street": "East Berkeley Street","description": "Washington St @ E Berkeley St - Silver Line - South Station/Downtown Crossing","latitude": 42.344189,"location_type": 0,"longitude": -71.065726,"municipality": "Boston","name": "Washington St @ E Berkeley St","on_street": "Washington Street","platform_code": null,"platform_name": "South Station/Downtown Crossing","vehicle_type": 3,"wheelchair_boarding": 1}}'

# Parse the JSON data
data = json.loads(json_data)

# Select the latitude value
latitude = data['attributes']['latitude']

print(latitude) # Output: 42.344189
In this example, the JSON data is stored in the json_data variable, and the json.loads() function is used to parse it into a Python dictionary. The 'latitude' value is then accessed by calling the key 'attributes', and then the key 'latitude'.