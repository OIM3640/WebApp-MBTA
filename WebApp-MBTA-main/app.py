from flask import Flask, request, redirect, url_for
from flask import render_template
from mbta_helper import find_stop_near 
from mbta_helper import get_temp
from mbta_helper import lat_map
from mbta_helper import lng_map

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        place_name = request.form['place_name']
        # perform calculation using place_name variable
        result = f"The place name you entered was: {place_name}"
        return redirect(url_for('nearest_mbta', place_name=place_name), code=307)

    return '''
        <form method="post">
            <p>Hello World!</p>
            <p>Please enter a place name to get the closest MBTA station:</p>
            <input type="text" id="place-name" name="place_name">
            <button type="submit">Submit</button>
        </form>
    '''




@app.route('/mbta_helper', methods=['POST'])
def nearest_mbta():
    place_name = request.form['place_name']
    stop, station_info = find_stop_near(place_name)
    temp = get_temp('boston')
    # perform calculation using place_name variable
    # station_info = render_template('form.html')
    if station_info == 1:
        result = f"The nearest MBTA station to <span style='text-decoration: underline;'>{place_name}</span> is <span style='font-weight: bold;'>{stop}</span> & it is <span style='color: red; text-decoration: none;'>wheelchair accessible</span>. The current temperature is <span style='color: brown;'>{temp} degrees</span>."


    else:
        result = f"The nearest MBTA station to <span style='text-decoration: underline;'>{place_name}</span> is <span style='font-weight: bold;'>{stop}</span> & it is <span style='color: red; text-decoration: none;'>NOT wheelchair accessible</span>. The current temperature is <span style='color: brown;'>{temp} degrees</span>."

    return result

@app.route('/map/', methods=['GET', 'POST'])
def hello_():
    if request.method == 'POST':
        place_name = request.form['place_name']
        # perform calculation using place_name variable
        result = f"The place name you entered was: {place_name}"
        return redirect(url_for('map', place_name=place_name), code=307)

    return '''
        <form method="post">
            <p>Hello World!, for a second time</p>
            <p>Please enter a place name for the google maps location:</p>
            <input type="text" id="place-name" name="place_name">
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/show_map/',methods=['POST'])
def map():
    place_name = request.form['place_name']
    lat, lng = lat_map(place_name), lng_map(place_name)
    html_map = f'<iframe src="https://maps.google.com/maps?q={lat},{lng}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>'
    return html_map




if __name__ == '__main__':
    app.run(debug=True)
