from flask import render_template

from teacher import app
from .model import setup, runtime, alldata, code, code2, journal, planning, playground

# connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("home.html", projects=setup())


# connects /hello path of server to render hello.html
@app.route('/hello/')
def hello_rooute():
    return render_template("hello.html", projects=setup())


# connects /flask path of server to render flask.html
@app.route('/flask/')
def flask_route():
    return render_template("flask.html", projects=setup())


@app.route("/project/runtime")
def runtime_route():
    return render_template("task.html", data=runtime())


@app.route("/project/planning")
def planning_route():
    return render_template("task.html", data=planning())


@app.route("/project/journal")
def journal_route():
    return render_template("task.html", data=journal())


@app.route("/project/playground")
def playground_route():
    return render_template("task.html", data=playground())


@app.route("/project/code")
def code_route():
    return render_template("task.html", data=code())


@app.route("/project/code2")
def code2_route():
    return render_template("task.html", data=code2())


@app.route("/all/")
def all_route():
    return render_template("taskall.html", datalist=alldata())


@app.route("/hey/")
def heyheyhey_route():
    return "<h1 style='background-color:blue;color:white'>Hey Hey Hey!</h1>"

@app.route("/maps/")
def maps_route():
    return render_template("maps.html")