from flask import Flask, render_template, request
from mbta_helper import main

import ssl
import urllib.request

app = Flask(__name__)


@app.route('/nearest', methods=['POST'])
def nearest_station():
    # use place_name to calcuate the nearest MBTA station
    place_name = request.form['place_name']

    # Retrun result to result.html template
    return render_template('result.html', station=nearest_station)


if __name__ == '__main__':
    app.run(debug=True)
