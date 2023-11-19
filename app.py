from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from mbta_helper import get_real_time_info

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['POST'])
def search():
    place_name = request.form['place_name']
    stop_name, is_accessible, stop_id = find_stop_near(place_name)
    real_time_data = get_real_time_info(stop_id)
    if real_time_data:
        arrival_time=real_time_data[0]
        status=real_time_data[1]
    else: 
        arrival_time = None
        status = None
    return render_template('result.html', place_name=place_name, stop_name=stop_name, is_accessible=is_accessible, arrival_time=arrival_time, status=status)

from flask import Flask, render_template


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')