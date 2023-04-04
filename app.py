from flask import Flask, render_template, request
from mbta_helper_draft import get_station

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.get('/mbta')
def mbta_get():
    return render_template('index.html')

@app.post('/mbta')
def mbta_post():
    location_name = request.form.get('query')
    station = get_station(location_name)
    return render_template('index.html', query = location_name, stop_name = station)



if __name__ == '__main__':
    app.run(debug=True)
