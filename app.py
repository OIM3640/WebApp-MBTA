"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mapquest import get_coordinates, get_location_info

from mbta import get_clostest_stop

from url import get_url


app = Flask(__name__)


@app.route('/nearest', methods=['GET'])
def get_location():
    return render_template('index.html')


@app.route('/nearest', methods=['POST'])
def get_nearest_stop():
    if request.form['location']:
        location = request.form['location']
        url = get_url(location)
        location_info = get_location_info(url)
        coordinates = get_coordinates(location_info)
        (lat, lng) = coordinates
        clostest_stop = get_clostest_stop(lat, lng)
        return render_template('result.html', location=location, clostest_stop=clostest_stop, coordinates=coordinates, url=url, location_info=location_info)


@app.route('/nearest')
def hello_world():
    return 'HelloWorld!'


if __name__ == '__main__':
    app.run(debug=True)
