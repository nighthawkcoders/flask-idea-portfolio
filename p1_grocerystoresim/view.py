from flask import render_template
from p1_grocerystoresim import p1_grocerystoresim_bp
from .model import runtime


@p1_grocerystoresim_bp.route('/')
def index():
    return render_template("groceryrun.html", data=runtime())


