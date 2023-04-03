from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['',''])
def show_station():
    return 'hello worldhhh!'


if __name__ == '__main__':
    app.run(debug=True)
