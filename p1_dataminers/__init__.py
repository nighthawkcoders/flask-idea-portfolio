from flask import Blueprint

p1_dataminers_bp = Blueprint(
    'p1_dataminers_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view