# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import render_template, url_for, redirect
from __init__ import app


@app.route('/')
def home_route():
    return render_template("base1.html")


@app.route('/period1/')
def period1_route():
    return render_template("period1.html")


@app.route('/period2/')
def period2_route():
    return render_template("period2.html")


@app.route('/period4/')
def period4_route():
    return render_template("period4.html")


@app.route('/period5/')
def period5_route():
    return render_template("period5.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='127.0.0.1', port='5001')
