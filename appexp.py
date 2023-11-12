from flask import Flask , render_template , request
from edits import find_stop_near

app = Flask(__name__)


@app.get('/')
def mbta_finder(name=None):
    return render_template('index.html', name=name) #functioning as intended.

#Based off code found on stack overflow link:https://stackoverflow.com/questions/43677564/passing-input-from-html-to-python-and-back
@app.post('/')
def hello():
    user_location_input = request.form['user_location_input']
    answer = find_stop_near(user_location_input)
    return f"{answer}"
if __name__ == '__main__':
    app.run(debug=True)