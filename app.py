from flask import Flask, render_template, request
import mbta_helper


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'Hello World!'

def home():
    if request.method == 'POST':
        address = request.form.get('address')
        mbta_helper.main(address)
    return render_template('index.html', message='Hello, World!')


if __name__ == '__main__':
    app.run(debug=True)
