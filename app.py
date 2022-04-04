"""
Simple "Hello, World" application using Flask
"""
#Importing all the required modules for the project
import urllib.request
import os
from flask import Flask, redirect, render_template, url_for

import requests
import urllib.request
import json
from pprint import pprint




#CREATING APP INSTANCE
app = Flask(__name__)

#Mapquesst API database interface
#User input for location stored in location variable 
#CREATING THE CALL FORMAT FOR THE MAPQUEST API
location = 'newyork'

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

api_key= '2d9525064b3444819a66dc7c40160dd2'
url = f'https://api-v3.mbta.com/docs/swagger/index.html'







@app.route('/')
def homepage():
    
   
    return render_template("ourwebsite.html")
    


@app.route('/form', methods=["POST"]) 
def form():
    title = "Thanks for using us!"
    located= requests.form.get("located")
    
    return render_template("form.html",title=title)   
    












if __name__ == '__main__':
    app.run(debug=True)
    #pprint(response_data['results'][0]['locations'][0]['latLng'])
    #print(response_data['results'][0]['locations'][0]['latLng']['lat'])