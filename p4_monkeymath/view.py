"""View in MVC has responsibility for interacting with user"""
# render_templates is only job required for view
from flask import render_template
# imports defintions of teacher blueprint from __init__.py
from p4_monkeymath import p4_monkeymath_bp
from p4_monkeymath import model


# connects default URL to a function
@p4_monkeymath_bp.route('/')
def home():
    # Flask import uses Jinga to render HTML
    return render_template("p4_monkeymath/home.html")


@p4_monkeymath_bp.route('/tetris/')
def tetris():
    return render_template("p4_monkeymath/tetris.html", projects=model.tetris())


@p4_monkeymath_bp.route('/mario/')
def mario():
    return render_template("p4_monkeymath/mario.html", projects=model.mario())


@p4_monkeymath_bp.route('/hangman/')
def hangman():
    return render_template("p4_monkeymath/hangman.html", projects=model.hangman())


@p4_monkeymath_bp.route('/pacman/')
def pacman():
    return render_template("p4_monkeymath/pacman.html", projects=model.pacman())


@p4_monkeymath_bp.route('/playground/')
def playground():
    return render_template("p4_monkeymath/playground.html", projects=model.playlist())


@p4_monkeymath_bp.route('/monkey/')
def monkey():
    return render_template("p4_monkeymath/monkey.html", projects=model.monkey())
