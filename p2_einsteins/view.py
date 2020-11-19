from p2_einsteins import model  # imports projects data from model.py

from flask import Flask, render_template  # imports the render template

app = Flask(__name__)

from p2_einsteins import p2_einsteins_bp


@p2_einsteins_bp.route('/')  # decorates the url with a route
def home_route():
    return render_template("plan.html", projects=model.setup())


@p2_einsteins_bp.route('/fundamentals/')
def fundamental_route():
    return render_template("fundamentals.html", projects=model.setup())
    # decoration passed through render_template of the setup in respective html file.


@p2_einsteins_bp.route('/calculator/')
def calculator_route():
    return render_template("calculator.html", projects=model.setup())


@p2_einsteins_bp.route('/ayman/')
def ayman_route():
    return render_template("ayman.html", projects=model.setup())


@p2_einsteins_bp.route('/pragadeesh/')
def pragadeesh_route():
    return render_template("pragadeesh.html", projects=model.setup())


@p2_einsteins_bp.route('/brandon/')
def brandon_route():
    return render_template("brandon.html", projects=model.setup())


@p2_einsteins_bp.route('/ali/')
def ali_route():
    return render_template("ali.html", projects=model.setup())


@p2_einsteins_bp.route('/navodit/')
def navodit_route():
    return render_template("navodit.html", projects=model.setup())


@p2_einsteins_bp.route('/journal/')
def journal_route():
    return render_template("journal.html", projects=model.setup())
