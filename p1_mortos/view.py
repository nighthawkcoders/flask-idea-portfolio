from flask import render_template
from p1_mortos import p1_mortos_bp
from .model import runtime

@p1_mortos_bp.route('/')
def index():
    return render_template("mortos.html", data=runtime())
    
