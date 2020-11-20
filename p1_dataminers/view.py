from flask import render_template
from p1_dataminers import p1_dataminers_bp
from .model import runtime

@p1_dataminers_bp.route('/')
def index():
    return render_template("dataminerrun.html", data=runtime())

