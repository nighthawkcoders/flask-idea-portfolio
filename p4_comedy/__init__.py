"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

p4_comedy_bp = Blueprint(
    'p4_comedy_bp',
    __name__,
    template_folder='templates',
)

from . import view
