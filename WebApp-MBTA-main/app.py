from flask import Flask, request, redirect, url_for
from flask import render_template
from mbta_helper import find_stop_near 
from mbta_helper import get_temp


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
            <p>Please enter a place name:</p>
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
        result = f"The nearest MBTA station to {place_name} is {stop} & it is wheelchair accesible. The current temperature is {temp} degrees."


    else:
        result = f"The nearest MBTA station to {place_name} is {stop} & it is NOT wheelchair accesible. The current temperature is {temp} degrees."

    return result

if __name__ == '__main__':
    app.run(debug=True)
