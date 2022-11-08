"""
Simple "Hello, World" application using Flask
"""

from flask import Flask


app = Flask(__name__)


from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


if __name__ == '__main__':
    app.run(debug=True)
