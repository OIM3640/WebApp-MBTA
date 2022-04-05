"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from mbta_helper import get_lat_long, get_nearest_station, find_stop_near


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
