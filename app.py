from flask import Flask, render_template, request, redirect, url_for
from mbta_helper import find_stop_near, get_nearest_station, get_temp

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def mbta_form():
    if request.method == 'POST':
        # location = request.form['location']
        location = request.form['current city']
        print(location)
        station_name, wheelchair_accessible = find_stop_near(location)
        return redirect(url_for('mbta_station', station_name=station_name, wc_accessible=wheelchair_accessible))
    
    return render_template('MBTA-form.html')

@app.route('/nearestMBTA/', methods=['POST'])
def nearest_mbta():
    location = request.form.get('MBTAlocation')
    # wheelchair_accessible = find_stop_near(location.replace(' ', '%20'))
    wheelchair_accessible = find_stop_near(location)

    return render_template('MBTA-result.html', MBTAlocation=location, wc_accessible=wheelchair_accessible)

@app.route('/mbtaStation/')
def mbta_station():
    station_name = request.args.get('station_name')
    wc_accessible = request.args.get('wc_accessible')
    

    return render_template('MBTA-result.html', station_name=station_name, wc_accessible=wc_accessible)

# we tried to complete the wow factor, but we kept receiving errors. Here is what we tried:


#@app.route('/mbtaStation/')
#def mbta_station():
    station_name = request.args.get('station_name')
    wc_accessible = request.args.get('wc_accessible')
    temperature = get_temp (station_name)
    

    return render_template('MBTA-result.html', station_name=station_name, wc_accessible=wc_accessible, temp=temperature)

# Essentially, we put the get_temp function into the mbta_helper.py so that it could access weather information from the API, but we kept getting errors.
# We think it might have something to do with the url but we are not sure


if __name__ == '__main__':
    app.run(debug=True)