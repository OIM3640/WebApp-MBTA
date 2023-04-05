from flask import Flask, render_template, request, redirect, url_for
from mbta_helper import find_stop_near, get_nearest_station

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mbta_form():
    if request.method == 'POST':
        location = request.form['location']
        station_name, wheelchair_accessible = get_nearest_station(location)
        return redirect(url_for('mbta_station', station_name=station_name, wc_accessible=wheelchair_accessible))
    
    return render_template('MBTA-form.html')

@app.route('/nearestMBTA/', methods=['POST'])
def nearest_mbta():
    location = request.form.get('MBTAlocation')
    wheelchair_accessible = find_stop_near(location.replace(' ', '%20'))
    return render_template('MBTA-result.html', MBTAlocation=location, wc_accessible=wheelchair_accessible)

@app.route('/mbtaStation/')
def mbta_station():
    station_name = request.args.get('station_name')
    wc_accessible = request.args.get('wc_accessible')
    return render_template('MBTA-station.html', station_name=station_name, wc_accessible=wc_accessible)

if __name__ == '__main__':
    app.run(debug=True)