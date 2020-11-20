"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

p5_chessGame_bp = Blueprint(
    'p5_chessGame_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view
#from . import modelChess

