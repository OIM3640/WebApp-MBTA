from mbta_helper import find_stop_near, get_lat_long, weather, get_nearest_station
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def home_page():
    return render_template('index.html')


# @app.post('/nearest')
# def nearest_station():
#     # use place_name to calcuate the nearest MBTA station
#     place_name = request.form.get('place_name')
#     stop, wheelchair = find_stop_near(place_name)

#     # Retrun result to result.html template
#     return render_template('result.html', place_name=place_name, nearest_stop=stop, wheelchair_accessible=wheelchair)


# @app.post('/map')
# def show_map():
#     place_name = request.form.get('place_name')
#     lat, lng = get_lat_long(place_name)
#     html_map = f'<iframe src="https://maps.google.com/maps?q={lat},{lng}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>'
#     return render_template('result.html', place_name=place_name, map=html_map)


# @app.post('/weather')
# def show_weather():
#     place_name = request.form.get('place_name')
#     temperature = weather(place_name)
#     return render_template('result.html', place_name=place_name, temperature=temperature)

@app.post('/results')
def results():
    place_name = request.form.get('place_name')
    stop, wheelchair = find_stop_near(place_name)
    #lat, lng = get_lat_long(place_name)# To show current Address

    # #trying to get the station location
    # try:
    #     clat, clng = get_lat_long(place_name)
    #     station, wh = get_nearest_station(clat, clng) #wh is irrelevant here
    #     lat, lng = get_lat_long(station)
    # except ValueError:
    #     print("Value Error")
    # if lat is not None:
    #     html_map = f'<iframe src="https://maps.google.com/maps?q={lat},{lng}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>'
    #     temperature = weather(place_name)
    # return render_template('result.html', place_name=place_name, nearest_stop=stop, wheelchair_accessible=wheelchair, map=html_map, temperature=temperature)
    # Initialize variables
    lat, lng = None, None
    html_map, temperature = "", ""

    # Get the coordinates for the place and the nearest station
    try:
        clat, clng = get_lat_long(place_name)
        station, wh = get_nearest_station(clat, clng)
        station = station + "massachusetts"
        lat, lng = get_lat_long(station)
    except ValueError:
        print("Value Error")

    if lat is not None and lng is not None:
        html_map = f'<iframe src="https://maps.google.com/maps?q={lat},{lng}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>'
        temperature = weather(place_name)

    return render_template('result.html', place_name=place_name, nearest_stop=stop, wheelchair_accessible=wheelchair, map=html_map, temperature=temperature)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
