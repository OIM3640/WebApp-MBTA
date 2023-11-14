from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from urllib.parse import quote

app = Flask(__name__)



@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

#Used ChatGPT to hyperlink Station Name to google maps for directions to station
@app.context_processor
def utility_processor():
    def generate_google_maps_link(location_name):
        # Replace spaces with '+' and encode the location name for the URL
        encoded_location = quote(location_name.replace(' ', '+'))
        return f'https://www.google.com/maps/search/?api=1&query={encoded_location}'

    return dict(generate_google_maps_link=generate_google_maps_link)


@app.route('/index', methods=['POST'])
def index():
    try:
        place_name = request.form.get('place', '').strip()
        if place_name:
            station_info = find_stop_near(place_name)
            return render_template('results.html', station_info=station_info)
        else:
            return render_template('index.html', error_message='Please enter a place name.')

    except Exception as e:
        error_message = str(e)
        return render_template('error.html', error_message=error_message)



if __name__ == '__main__':
    app.run(debug=True)