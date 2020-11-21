from flask import Blueprint

p5_pokemon_bp = Blueprint(
    'p5_pokemon_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view