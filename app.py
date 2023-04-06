from flask import Flask, render_template, request
from mbta_helper import get_station
from mbta_helper import mbta_coord

app = Flask(__name__)


# @app.route('/mbta', methods=['GET', 'POST'])
@app.get('/mbta')
def mbta_get():
    return render_template('index.html')
@app.post('/mbta')
def mbta_post():
    location_name = request.form.get('query')
    station = get_station(location_name.replace(' ', '%20'))
    lat, lng = mbta_coord(location_name.replace(' ','%20'))
    html_map = f'<iframe src="https://maps.google.com/maps?q={lat},{lng}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"<</iframe>'
    print(html_map)
    return render_template('result.html', location_name = location_name, station_0 = station[0], station_1 = station[1], station_2 = station[2], html_map = html_map)    


if __name__ == '__main__':
    app.run(debug=True)
