"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/nearest_mbta/',methods=["GET","POST"])
def get_station():
    if request.method == "POST":
        place_name=request.form["place"]
        station_name, wheel_chair=find_stop_near(place_name)
        return render_template("station_result.html",place=place_name,station=station_name,wheel=wheel_chair)
    return render_template("station_form.html")

@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
