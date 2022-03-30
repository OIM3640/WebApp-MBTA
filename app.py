"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'YOUR API KEY'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
