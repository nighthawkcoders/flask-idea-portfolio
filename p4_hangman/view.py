"""View in MVC has responsibility for interacting with user"""
# render_templates is only job required for view
from flask import render_template
# imports defintions of teacher blueprint from __init__.py
from p4_hangman import p4_hangman_bp
# imports from model each data definition
from .model import setup, playlist


# Create a sign up page
@p4_hangman_bp.route('/')
def index():
    return render_template("home2.html", projects=setup())


# connects /hello path of server to render hello2.html


@p4_hangman_bp.route('/hello2/')
def hello2_route():
    return render_template("hello2.html", projects=setup())


# connects /flask path of server to render flask2.html


@p4_hangman_bp.route('/flask2/')
def flask2_route():
    return render_template("flask2.html", projects=setup())


@p4_hangman_bp.route('/about2/')
def about2_route():
    return render_template("about2.html", datalist2=playlist())

# Create a sign up page


@p4_hangman_bp.route('/music/')
def signup_route():
    return render_template("homemusic.html", projects=setup())

# connects /hello path of server to render hello2.html


@p4_hangman_bp.route('/rock/')
def rock_route():
    return render_template("rock.html", projects=setup())

# connects /flask path of server to render flask2.html


@p4_hangman_bp.route('/jazz/')
def jazz_route():
    return render_template("jazz.html", projects=setup())


@p4_hangman_bp.route('/pop/')
def pop_route():
    return render_template("pop.html", projects=setup())
