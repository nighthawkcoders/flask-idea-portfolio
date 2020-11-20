from p4_fruitycoders import p4_fruitycoders_bp
from flask import Flask, render_template

app = Flask(__name__)

@p4_fruitycoders_bp.route('/')
def index():
    return render_template("p4_fruitycoders/home.html")


@p4_fruitycoders_bp.route('/history/')
def history_route():
    return render_template("p4_fruitycoders/history.html")


@p4_fruitycoders_bp.route('/biographies/')
def biographies_route():
    return render_template("p4_fruitycoders/biographies.html")


@p4_fruitycoders_bp.route('/aboutus/')
def aboutus_route():
    return render_template("p4_fruitycoders/aboutus.html")


@p4_fruitycoders_bp.route('/adams/')
def adams_route():
    return render_template("p4_fruitycoders/adams.html")


@p4_fruitycoders_bp.route('/bourke/')
def bourke_route():
    return render_template("p4_fruitycoders/bourke.html")


@p4_fruitycoders_bp.route('/goldin/')
def goldin_route():
    return render_template("p4_fruitycoders/goldin.html")


@p4_fruitycoders_bp.route('/leibovitz/')
def leibovitz_route():
    return render_template("p4_fruitycoders/leibovitz.html")


@p4_fruitycoders_bp.route('/mann/')
def mann_route():
    return render_template("p4_fruitycoders/mann.html")


@p4_fruitycoders_bp.route('/mccurry/')
def mccurry_route():
    return render_template("p4_fruitycoders/mccurry.html")


@p4_fruitycoders_bp.route('/newman/')
def newman_route():
    return render_template("p4_fruitycoders/newman.html")


@p4_fruitycoders_bp.route('/pretty/')
def pretty_route():
    return render_template("p4_fruitycoders/pretty.html")


@p4_fruitycoders_bp.route('/shabazz/')
def shabazz_route():
    return render_template("p4_fruitycoders/shabazz.html")


@p4_fruitycoders_bp.route('/wong/')
def wong_route():
    return render_template("p4_fruitycoders/wong.html")
