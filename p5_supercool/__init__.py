"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

teacher_bp = Blueprint(
    'p5_supercool_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view
