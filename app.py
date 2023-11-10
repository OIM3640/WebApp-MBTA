from flask import Flask, render_template, request
from main import your_closest_station
import pprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html/')

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.post('/')
def stations_post():
    query = request.form['QUERY']
    return print(f'{your_closest_station(query)}')

if __name__ == '__main__':
    app.run(debug=True)
