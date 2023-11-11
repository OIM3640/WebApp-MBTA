from flask import Flask, render_template, request
from main import your_closest_station

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html/')

@app.route('/result', methods=['POST'])
def result():
    data_from_form = request.form['QUERY']
    result = your_closest_station(data_from_form)
    return render_template('/result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
