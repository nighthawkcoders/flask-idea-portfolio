"""View in MVC has responsibility for interacting with user"""
# render_templates is only job required for view
from flask import render_template
# imports defintions of teacher blueprint from __init__.py
from p1_robotmania import p1_robotmania_bp
# imports from model each data definition
from .model import p1robotmania


# connects default URL of server to render plan.html
@p1_robotmania_bp.route('/')
def index():
    return render_template("robotmaniarun.html", data=p1robotmania())


