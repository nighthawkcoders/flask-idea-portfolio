from flask import Flask, redirect, url_for, render_template
from p5_supercool import p5_supercool_bp, scraping, Data

app = Flask(__name__)


@p5_supercool_bp.route("/landing")
@app.route("/")
def landing():
    return render_template("gg-landing.html")


@p5_supercool_bp.route("/home")
@app.route("/")
def home():
    return render_template("gg-home.html")


@p5_supercool_bp.route("/covid")
@app.route("/")
def covid():
    return render_template("gg-covid.html", data=scraping.countrydata(), data1=scraping.worldtotal())


@p5_supercool_bp.route("/p5")
@app.route("/")
def p5():
    return render_template("gg-p5.html")


@p5_supercool_bp.route("/history")
@app.route("/")
def history():
    return render_template("gg-history.html")


@p5_supercool_bp.route("/geoguesser")
def geoguesser():
    return render_template("geoguesser.html", data=Data.inputdata1(), data1=Data.inputdata2(), data2=Data.picran())


# ===================================================================================

@p5_supercool_bp.route("/africa")
@app.route("/")
def africa():
    return render_template("history-africa.html")


@p5_supercool_bp.route("/america")
@app.route("/")
def america():
    return render_template("history-america.html")


@p5_supercool_bp.route("/brazil")
@app.route("/")
def brazil():
    return render_template("history-brazil.html")


@p5_supercool_bp.route("/denmark")
@app.route("/")
def denmark():
    return render_template("history-denmark.html")


@p5_supercool_bp.route("/greece")
@app.route("/")
def greece():
    return render_template("history-greece.html")


@p5_supercool_bp.route("/iceland")
@app.route("/")
def iceland():
    return render_template("history-iceland.html")


@p5_supercool_bp.route("/india")
@p5_supercool_bp.route("/")
def india():
    return render_template("history-india.html")

# ===================================================================================
