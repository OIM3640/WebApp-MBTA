from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/search', methods=['POST'])
def search():
    place_name = request.form['place_name']
    stop_name, stop_accessible = find_stop_near(place_name)
    return render_template('results2.html', stop_name=stop_name, stop_accessible=stop_accessible)

if __name__ == "__main__":
    app.run(debug=True)
