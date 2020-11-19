"""View in MVC has responsibility for interacting with user"""
# render_templates is only job required for view
from flask import render_template
# imports defintions of teacher blueprint from __init__.py
from p5_bang2 import p5_bang2_bp
# imports from model each data definition
from .model import p5_bang2


# connects default URL of server to render home.html
@p5_bang2_bp.route('/')
def index():
    return render_template("bang2.html", data=p5_bang2())