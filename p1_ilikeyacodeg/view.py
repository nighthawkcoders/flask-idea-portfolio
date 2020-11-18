from flask import render_template
from p1_ilikeyacodeg import p1_ilikeyacodeg_bp
from .model import runtime

@p1_ilikeyacodeg_bp.route('/')
def index():
    return render_template("ilike.html", data=runtime())


