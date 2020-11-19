"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

p2_rappers_bp = Blueprint(
    'p2_rappers_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view
