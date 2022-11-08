"""
This is an application to help find the nearest MBTA stop near the user and whether it is wheelchair accessible using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/',method=['GET', 'POST'])
def location():
    """Ask user for a place name, return the nearest MBTA stop and wheelchair accessible information"""
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
