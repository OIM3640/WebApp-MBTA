from flask import Flask, render_template, request, redirect
from main import your_closest_station

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html/')

@app.route('/result', methods=['POST'])
def result():
    data_from_form = request.form['QUERY']
    query = data_from_form
    result = str(your_closest_station(data_from_form))
    formatted_result = result[2:len(result)-2]
    return render_template('/result.html', result=formatted_result, query = query)

@app.route('/redirect', methods = ['GET'])
def redirect_home():
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
