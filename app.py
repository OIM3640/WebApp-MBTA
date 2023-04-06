from flask import Flask, render_template, request
from mbta_helper import get_station
from mbta_helper import mbta_coord

app = Flask(__name__)


@app.route('/mbta', methods=['GET', 'POST'])
def mbta_form():
    if request.method == 'POST':
        location_name = request.form.get('query')
        station = get_station(location_name.replace(' ', '%20'))
        return f'The closest station to {location_name} is stop {station[0]} on {station[2]} and it is {station[1]}.'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
