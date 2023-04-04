from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

# , methods=['','']
@app.route('/')
def show_station():
    return render_template("index.html")

@app.post("/nearest_mbta")
def station_post():
    place_name = request.form.get["place"]
    station = find_stop_near(place_name)
    return render_template("station-result.html", place = place_name, station = station)

if __name__ == '__main__':
    app.run(debug=True)
