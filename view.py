"""View/Control in frontend/backend, view & control according to classic MVC guidelines Pedro"""

from flask import render_template

from __init__ import app
import data_p1, data_p2, data_p4, data_p5  # projects definitions are placed in different file


@app.route('/')
def home_route():
    return render_template("base1.html")


@app.route('/period1/')
def period1_route():
    return render_template("period.html", period=data_p1.setup())


@app.route('/period2/')
def period2_route():
    return render_template("period.html", period=data_p2.setup())


@app.route('/period4/')
def period4_route():
    return render_template("period.html", period=data_p4.setup())


@app.route('/period5/')
def period5_route():
    return render_template("period.html", period=data_p5.setup())
