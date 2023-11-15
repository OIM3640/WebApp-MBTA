from flask import Flask, render_template, request
import mbta_helper2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        address = request.form.get('address')
        
        # Validate the address
        if not address:
            return render_template('index.html', message='Please enter a valid address.')

        # Call mbta_helper2 to get the data
        station_name, wheelchair_accessible, map_url = mbta_helper2.find_stop_near(address)

        if station_name:
            return render_template('result.html', station_name=station_name, wheelchair_accessible=wheelchair_accessible, map_url=map_url)
        else:
            return render_template('index.html', message='No MBTA stop found for the given address.')

    return render_template('index.html', message='')

if __name__ == '__main__':
    app.run(debug=True)