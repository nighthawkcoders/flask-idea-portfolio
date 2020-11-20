from flask import Blueprint

p1_asciimenu_bp = Blueprint(
    'p1_asciimenu_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view