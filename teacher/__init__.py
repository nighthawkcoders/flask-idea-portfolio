# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask  # create a Flask instance

app = Flask(__name__)

import teacher.view

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port="8080", host="127.0.0.1")
