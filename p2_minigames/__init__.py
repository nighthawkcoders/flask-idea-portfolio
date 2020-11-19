"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

minigames_bp = Blueprint(
    'minigames_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)
app.register_blueprint(p2_minigames_bp, url_prefix=’/p2_minigames’)
