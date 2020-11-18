from flask import Blueprint

p4_slackbots_bp = Blueprint(
    'p4_slackbots_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view