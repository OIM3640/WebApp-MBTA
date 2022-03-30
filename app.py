"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from ppcode import get_lat, get_lng

app = Flask(__name__)

@app.route('/nearest_mbta/',methods=["GET","POST"])
def get_station():
    if request.method == "POST":
        city_name=request.form["city"]
        lat=get_lat(city_name)
        lng=get_lng(city_name)
        
        return render_template("station_result.html",)
@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
