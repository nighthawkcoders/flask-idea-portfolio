from flask import render_template
from p1_hexpass import p1_hexpass_bp
from .model import runtime


@p1_hexpass_bp.route('/')
def index():
    return render_template("task.html", data=runtime())