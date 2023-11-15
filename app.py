from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['POST'])
def search_mbta():
    if request.method=="POST":
        place_name = request.form['place_name']
        
        stop_name, is_accessible = find_stop_near(place_name)
        
        return render_template('result.html', place_name=place_name, stop_name=stop_name, is_accessible=is_accessible)

    else: 
        return render_template("404.html")
    
if __name__ == '__main__':
    app.run(debug=True)