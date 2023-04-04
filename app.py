from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from mbta_helper import get_weather

app = Flask(__name__)

@app.get('/station/')
def station_get():
    return render_template('station-form.html', error=None)

@app.post('/station/')
def station_post():
    place_name = str(request.form["place_name"])
    route_type = str(request.form['route_type'])
    station, wheelchair_accessible = find_stop_near(place_name, route_type)
    weather, temperature = get_weather(place_name)

    if wheelchair_accessible == 0:
        wheelchair = 'No Information'
    elif wheelchair_accessible == 1:
        wheelchair = 'Accessible'
    else:
        wheelchair = 'Inaccessible'
        
    if station:
        return render_template('station-result.html', place=place_name, station=station, wheelchair=wheelchair, route=route_type, weather = weather, temperature=temperature)
    else:
        return render_template('station-form.html', error=True)





@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
