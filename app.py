from flask import Flask, render_template, request
from mbta_helper import get_station


app = Flask(__name__)


@app.route('/mbta', methods=['GET', 'POST'])
def mbta_form():
    if request.method == 'POST':
        location_name = request.form.get('query')
        station = get_station(location_name.replace(' ', '%20'))
        return f'The closest station to {location_name} is stop {station[0]} and it is {station[1]}.'
    return render_template('index.html')

# @app.route('/map')
# def show_map():
#     lat, lng = get_lat_long('query')
#     html_map = f'<iframe src="https://maps.google.com/maps?q={lat},{lng}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>'
#     return html_map



if __name__ == '__main__':
    app.run(debug=True)
