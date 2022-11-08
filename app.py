"""
Simple "Hello, World" application using Flask
"""

from flask import Flask


app = Flask(__name__)


from flask import request

# 1. 
# Hello page + input form
# 2. 
# @app post/nearest post request
# 3.  
# Render a page present result from part 1
# 4. 
# Or error page say the search did not work + button(link) redirect to the first page



if __name__ == '__main__':
    app.run(debug=True)
