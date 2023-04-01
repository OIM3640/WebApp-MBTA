from flask import Flask, render_template, request
from mbta_helper import main

import ssl
import urllib.request

app = Flask(__name__)

@app.route('/')
def mbta_helper():
    return render_template('index.html')

@app.get('/input/')
def get_location():
    return render_template('index.html')

@app.post('/input/')
def post_location():
    place_name = request.form['place']
    return render_template('index.html', place=place_name)

if __name__ == '__main__':
    app.run(debug=True)

