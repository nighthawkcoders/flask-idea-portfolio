"""_init_.py is used to define app and all blueprints"""
from flask import Flask
app = Flask(__name__)

# Period 1
from p1_dataminers import p1_dataminers_bp
app.register_blueprint(p1_dataminers_bp, url_prefix='/p1_dataminers')

from p1_grocerystoresim import p1_grocerystoresim_bp
app.register_blueprint(p1_grocerystoresim_bp, url_prefix='/p1_grocerystoresim')

from p1_ilikeyacodeg import p1_ilikeyacodeg_bp
app.register_blueprint(p1_ilikeyacodeg_bp, url_prefix='/p1_ilikeyacodeg')

from p1_mortos import p1_mortos_bp
app.register_blueprint(p1_mortos_bp, url_prefix='/p1_mortos')

from p1_robotmania import p1_robotmania_bp
app.register_blueprint(p1_robotmania_bp, url_prefix='/p1_robotmania')

from p1_hexpass import p1_hexpass_bp
app.register_blueprint(p1_hexpass_bp, url_prefix='/p1_hexpass')

from p1_asciimenu import p1_asciimenu_bp
app.register_blueprint(p1_asciimenu_bp, url_prefix='/p1_asciimenu')

# Period 2
from p2_cyphercrypto import cyphercrypto_bp
app.register_blueprint(cyphercrypto_bp, url_prefix='/p2_cyphercrypto')

from p2_dinos import p2_dinos_bp
app.register_blueprint(p2_dinos_bp, url_prefix='/p2_dinos')

from p2_triviagame import p2_triviagame_bp
app.register_blueprint(p2_triviagame_bp, url_prefix='/p2_triviagame')

# Period 4
from p4_slackbots import p4_slackbots_bp
app.register_blueprint(p4_slackbots_bp, url_prefix='/p4_slackbots')

from p4_hangman import p4_hangman_bp
app.register_blueprint(p4_hangman_bp, url_prefix='/p4_hangman')

from p4_fruitycoders import p4_fruitycoders_bp
app.register_blueprint(p4_fruitycoders_bp, url_prefix='/p4_fruitycoders')

from p4_coderjoes import p4_coderjoes_bp
app.register_blueprint(p4_coderjoes_bp, url_prefix='/p4_coderjoes')

from p4_monkeymath import p4_monkeymath_bp
app.register_blueprint(p4_monkeymath_bp, url_prefix='/p4_monkeymath')

from p4_charlieb import p4_charlieb_bp
app.register_blueprint(p4_charlieb_bp, url_prefix='/p4_charlieb')

#from p4_comedy import p4_comedy_bp
#app.register_blueprint(p4_comedy_bp, urlprefix='/p4_comedy')

# Period 5
from p5_supercool import p5_supercool_bp
app.register_blueprint(p5_supercool_bp, url_prefix='/p5_supercool')

from p5_alethianews import p5_alethianews_bp
app.register_blueprint(p5_alethianews_bp, url_prefix='/p5_alethianews')

from p5_monkeymen import p5_monkeymen_bp
app.register_blueprint(p5_monkeymen_bp, url_prefix='/p5_monkeymens')

from p5_calculus import p5_calculus_bp
app.register_blueprint(p5_calculus_bp, url_prefix='/p5_calculus')

from p5_chessGame import p5_chessGame_bp
app.register_blueprint(p5_chessGame_bp, url_prefix='/p5_chessGame')

from p2_einsteins import p2_einsteins_bp
app.register_blueprint(p2_einsteins_bp, url_prefix='/p2_einsteins')

from p2_rappers import p2_rappers_bp
app.register_blueprint(p2_rappers_bp, url_prefix='/p2_rappers')

from p5_multimedia import p5_multimedia_bp
app.register_blueprint(p5_multimedia_bp, url_prefix='/p5_multimedia')

from p5_pokemon import p5_pokemon_bp
app.register_blueprint(p5_pokemon_bp, url_prefix='/p5_pokemon')
