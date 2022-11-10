from flask import *
from mbta_helper import find_stop_near 
from ticketmaster import get_event_near

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = (request.form['name'])
        ((_location , _accessible), _error) = find_stop_near(name)
        return render_template('index.html', location=_location, accessible=_accessible, error=_error)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
    app.config['DEBUG'] = True