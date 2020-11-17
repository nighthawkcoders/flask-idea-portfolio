"""View in MVC has responsibility for interacting with user Karam"""
# render_templates is only job required for view
from flask import render_template
# imports defintions of teacher blueprint from __init__.py
from teacher import teacher_bp
# imports from model each data definition
from .model import setup, runtime, alldata, code, code2, journal, planning, playground, calculatorgui


# connects default URL of server to render home.html
@teacher_bp.route('/')
def index():
    return render_template("home.html", projects=setup())


# connects /hello path of server to render hello.html
@teacher_bp.route('/hello/')
def hello_route():
    return render_template("hello.html", projects=setup())


# connects /flask path of server to render flask.html
@teacher_bp.route('/flask/')
def flask_route():
    return render_template("flask.html", projects=setup())


@teacher_bp.route("/project/runtime/")
def runtime_route():
    return render_template("task.html", data=runtime())


@teacher_bp.route("/project/planning/")
def planning_route():
    return render_template("task.html", data=planning())


@teacher_bp.route("/project/journal/")
def journal_route():
    return render_template("task.html", data=journal())


@teacher_bp.route("/project/playground/")
def playground_route():
    return render_template("task.html", data=playground())


@teacher_bp.route("/project/code/")
def code_route():
    return render_template("task.html", data=code())


@teacher_bp.route("/project/code2/")
def code2_route():
    return render_template("task.html", data=code2())


@teacher_bp.route("/project/calculatorgui/")
def calculatorgui_route():
    return render_template("task.html", data=calculatorgui())


@teacher_bp.route("/about/")
def about_route():
    return render_template("taskall.html", datalist=alldata())


@teacher_bp.route("/maps/")
def maps_route():
    return render_template("maps.html")
