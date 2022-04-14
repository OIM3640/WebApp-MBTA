
#Importing all the required modules for the project
import urllib.request
import os
from flask import Flask, redirect, render_template, url_for,Request,request


import requests

import json
from pprint import pprint




#CREATING APP INSTANCE
app = Flask(__name__)

#Mapquesst API database interface
#User input for location stored in location variable 
#CREATING THE CALL FORMAT FOR THE MAPQUEST API
location = 'newyork'
#testing API
MAPQUEST_API_KEY = 'VOkvo2bQdXve8kGHbBxzvQhJDzc6lpfG'
url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
#pprint(response_data)
#gets lat and long from data output
#{'lat': 42.29822, 'lng': -71.26543}>> Format, specify [lat] or [lng]
response_data['results'][0]['locations'][0]['latLng']


#SECOND API, CREATING THE CALL FORMAT FOR THE MBTA API
#testing API
lat = 42.358894
lng = -71.056742
url1 = f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}" 
g = urllib.request.urlopen(url1)
response_text2 = g.read().decode('utf-8')
response_data2 = json.loads(response_text2)



# def homepage():
    
   
#return render_template("ourwebsite.html",)
    



#main app route (homepage, response page )

@app.route('/', methods=["GET","POST"])
def form():
    if request.method == "POST":
        located= (request.form["located"])

        location = located.replace(" ",'%20')
        location =location + ',Ma' 
        
        MAPQUEST_API_KEY = 'VOkvo2bQdXve8kGHbBxzvQhJDzc6lpfG'
        url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
        f = urllib.request.urlopen(url)
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        lat = response_data['results'][0]['locations'][0]['latLng']['lat']
        lng = response_data['results'][0]['locations'][0]['latLng']['lng']
        coordinates = [lat,lng]
        #Second API call
        url1 = f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}" 
        g = urllib.request.urlopen(url1)
        response_text2 = g.read().decode('utf-8')
        response_data2 = json.loads(response_text2)
        response_data2['data']
        neareststation = str(response_data2['data'][0]['attributes']['at_street'])
        #Conditional to determine if the location is wheelchair accesible
        if response_data2['data'][0]['attributes']['wheelchair_boarding'] == 1:
            wheelchair = 'Yes'
        else: wheelchair = 'No'
        return render_template("form.html",distance = neareststation,wheelchairs= wheelchair) 
    return render_template("ourwebsite.html")

    
    
   












if __name__ == '__main__':
    app.run(debug=True)
    #pprint(response_data['results'][0]['locations'][0]['latLng'])
    #print(response_data['results'][0]['locations'][0]['latLng']['lat'])
    ##print(response_data2['data'][0]['attributes']['at_street'])
