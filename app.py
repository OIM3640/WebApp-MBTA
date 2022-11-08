"""
This is an application to help find the nearest MBTA stop near the user and whether it is wheelchair accessible using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from get_weather import get_temp


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def get_location_and_weather():
    """Ask user for a place name, return the nearest MBTA stop and wheelchair accessible information"""
    if request.method == 'POST':
        location = request.form['location']
        station_name, wheelchair_accessible = find_stop_near(location)
        temperature = get_temp('Boston')
        return render_template('result.html', station = station_name, wheelchair = wheelchair_accessible, temp = temperature)
    
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
