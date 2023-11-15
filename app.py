from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!', render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form['input_data']
        return render_template('index.html', input_data=input_data)
    return render_template('index.html')

@app.get('/nearest_mbta')
def mbta_get():
    return render_template('index.html')

@app.post('/nearest_mbta')
def mbta_post():
    if request.method == 'POST':
        city_name = request.form['city_name']
        nearest_station = find_stop_near(city_name)
        return f'The nearest MBTA station for {city_name} is {nearest_station}.'

if __name__ == '__main__':
    app.run(debug=True)

