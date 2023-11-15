from flask import Flask, render_template, request
from mbta_helper2 import find_stop_near

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        address = request.form.get('address')
        station_name, wheelchair_accessible = find_stop_near(address)
        
        if station_name is not None:
            return render_template('results.html', station_name=station_name, wheelchair_accessible=wheelchair_accessible)
        else:
            return render_template('index.html', message='No results found. Please try again.')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

