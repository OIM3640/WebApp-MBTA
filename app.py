"""LUKE PATA"""
import mbta_helper
from flask import Flask, render_template, request
from mbta_helper import get_json, get_lat_long, get_nearest_station, get_temp, find_stop_near



app = Flask(__name__)

@app.route('/mbta/')

@app.get('/mbta/')
def close_station_get():
    return render_template('index.html')

@app.post('/mbta/')
def close_station_post():
    location = request.form['Current Location']
    lat_and_long = get_lat_long(location)
    get_near = get_nearest_station(lat_and_long)  # returns name_accessible tuple
    if get_near == "Problem":
        return "There was a problem, please try a differnet location."
    station = get_nearest_station(lat_and_long)[0]
    accessible = get_nearest_station(lat_and_long)[1]
    hidden = ""
    if accessible == 0:
        accessible = "(No Information)"
    elif accessible == 1:
        accessible = "accessible"
    else:
        accessible = "inaccessible"
    temp = get_temp('Boston')

    if location == 'Fenway Park': #hidden message for those going to catch a game
        hidden = "Go Sox's!"
    else:
        pass

    return render_template('index_result.html', station=station, accessible=accessible, temp=temp, hidden=hidden)


if __name__ == '__main__':
    app.run(debug=True)
