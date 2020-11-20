# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
# create a Flask instance
from p5_alethianews import p5_alethianews_bp

#app = Flask(__name__)


# connects default URL of server to a python function
@p5_alethianews_bp.route('/')
def index():
    # function use Flask import (Jinga) to render an HTML template
    return render_template("p5_alethianews/home.html")


