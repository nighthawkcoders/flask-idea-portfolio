from flask import Flask, redirect, url_for, render_template
from p5_supercool import p5_supercool_bp, scraping, Data

app = Flask(__name__)

@p5_supercool_bp.route("/landing")
def landing():
    return render_template("p5_supercool/gg-landing.html")

@p5_supercool_bp.route("/home")
def home():
    return render_template("p5_supercool/gg-home.html")


@p5_supercool_bp.route("/covid")
def covid():
    return render_template("p5_supercool/gg-covid.html", data=scraping.countrydata(), data1=scraping.worldtotal())


@p5_supercool_bp.route("/p5")
def p5():
    return render_template("p5_supercool/gg-p5.html")


@p5_supercool_bp.route("/history")
def history():
    return render_template("p5_supercool/gg-history.html")


@p5_supercool_bp.route("/geoguesser")
def geoguesser():
    return render_template("p5_supercool/geoguesser.html", data=Data.inputdata1(), data1=Data.inputdata2(), data2=Data.picran())


# ===================================================================================

@p5_supercool_bp.route("/africa")
def africa():
    return render_template("p5_supercool/history-africa.html")


@p5_supercool_bp.route("/america")
def america():
    return render_template("p5_supercool/history-america.html")


@p5_supercool_bp.route("/brazil")
def brazil():
    return render_template("p5_supercool/history-brazil.html")


@p5_supercool_bp.route("/denmark")
def denmark():
    return render_template("p5_supercool/history-denmark.html")


@p5_supercool_bp.route("/greece")
def greece():
    return render_template("p5_supercool/history-greece.html")


@p5_supercool_bp.route("/iceland")
def iceland():
    return render_template("p5_supercool/history-iceland.html")


@p5_supercool_bp.route("/india")
def india():
    return render_template("p5_supercool/history-india.html")

# ===================================================================================
