from flask import render_template
from p1_thecoders import p1_thecoders_bp
from .model import runtime

@p1_thecoders_bp.route('/')
def index():
    return render_template("task.html", data=runtime())