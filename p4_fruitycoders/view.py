from flask import Flask, render_template
from p4_fruitycoders import p4_fruitycoders_bp

app = Flask(__name__)


@p4_fruitycoders_bp.route('/')
def home_route():
    return render_template("home.html")


@p4_fruitycoders_bp.route('/history/')
def hello_route():
    return render_template("history.html")


@p4_fruitycoders_bp.route('/biographies/')
def biographies_route():
    return render_template("biographies.html")


@p4_fruitycoders_bp.route('/aboutus/')
def aboutus_route():
    return render_template("aboutus.html")


@p4_fruitycoders_bp.route('/adams/')
def adams_route():
    return render_template("adams.html")


@p4_fruitycoders_bp.route('/bourke/')
def bourke_route():
    return render_template("bourke.html")


@p4_fruitycoders_bp.route('/goldin/')
def goldin_route():
    return render_template("goldin.html")


@p4_fruitycoders_bp.route('/leibovitz/')
def leibovitz_route():
    return render_template("leibovitz.html")


@p4_fruitycoders_bp.route('/mann/')
def mann_route():
    return render_template("mann.html")


@p4_fruitycoders_bp.route('/mccurry/')
def mccurry_route():
    return render_template("mccurry.html")


@p4_fruitycoders_bp.route('/newman/')
def newman_route():
    return render_template("newman.html")


@p4_fruitycoders_bp.route('/pretty/')
def pretty_route():
    return render_template("pretty.html")


@p4_fruitycoders_bp.route('/shabazz/')
def shabazz_route():
    return render_template("shabazz.html")


@p4_fruitycoders_bp.route('/wong/')
def wong_route():
    return render_template("wong.html")
