from flask import Flask, render_template, request
import mbta_helper as mh


app = Flask(__name__)

# @app.route('/mbta', methods=['GET', 'POST'])
@app.get('/')
def mbta_get():
    return render_template('index.html')

@app.post('/')
def mbta_post():
    location_name = request.form.get('query')
    station = mh.find_stop_near(location_name)
    return render_template('index.html', query = location_name, stop_name = station)

  





if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)
