from flask import *
from mbta_helper import find_stop_near 
from ticketmaster import get_event_near
# from ticketmaster import get_events

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = (request.form['name'])
        ((_location , _accessible), _error) = find_stop_near(name)
        ((_event_name , _event_venue, _event_link), _event_error) = get_event_near(name)
        _res_error = _error or _event_error
        return render_template('index.html', location=_location, accessible=_accessible, error=_res_error, event_name = _event_name, event_venue = _event_venue, event_link = _event_link)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
    app.config['DEBUG'] = True