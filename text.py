import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1IjoibWlrZXN3aWVyIiwiYSI6ImNsb3E4OXp4djA0aWQya21rdzN3YXk0MHcifQ.Y7Sv0ziTdOh6Zn2Fo417nA'
query = 'Babson College'
query = query.replace(' ', '%20') # In URL encoding, spaces are typically replaced with "%20"
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url) # Try this URL in your browser first

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint.pprint(response_data['features'][0]['geometry']['coordinates'])

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     try:
#         if request.method == 'POST':
#             place_name = request.form.get('place_name', '').strip()
#             if place_name:
#                 station_info = find_stop_near(place_name)
#                 return render_template('results.html', station_info=station_info)
#             else:
#                 return render_template('index.html', error_message='Please enter a place name.')

#         return render_template('index.html')

#     except Exception as e:
#         error_message = str(e)
#         return render_template('error.html', error_message=error_message)

# # ... Other route and setup code ...

# if __name__ == '__main__':
#     app.run(debug=True)