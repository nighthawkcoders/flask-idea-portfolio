"""_init_.py is used to define app and all blueprints"""
from flask import Flask
app = Flask(__name__)

# Period 1
#from teacher import teacher_bp
#app.register_blueprint(teacher_bp, url_prefix='/teacher')

from p1_dataminers import p1_dataminers_bp
app.register_blueprint(p1_dataminers_bp, url_prefix='/p1_dataminers')

from p1_ilikeyacodeg import p1_ilikeyacodeg_bp
app.register_blueprint(p1_ilikeyacodeg_bp, url_prefix='/p1_ilikeyacodeg')

from p1_mortos import p1_mortos_bp
app.register_blueprint(p1_mortos_bp, url_prefix='/p1_mortos')

from p1_robotmania import p1_robotmania_bp
app.register_blueprint(p1_robotmania_bp, url_prefix='/p1_robotmania')

# Period 2
from p2_cyphercrypto import cyphercrypto_bp
app.register_blueprint(cyphercrypto_bp, url_prefix='/p2_cyphercrypto')

from p2_einsteins import p2_einsteins_bp
app.register_blueprint(p2_einsteins_bp, url_prefix='/p2_einsteins')

# Period 4
from p4_slackbots import p4_slackbots_bp
app.register_blueprint(p4_slackbots_bp, url_prefix='/p4_slackbots')

from p4_hangman import p4_hangman_bp
app.register_blueprint(p4_hangman_bp, url_prefix='/p4_hangman')

from p4_coderjoes import p4_coderjoes_bp
app.register_blueprint(p4_coderjoes_bp, url_prefix='/p4_coderjoes')

# Period 5
from p5_chessGame import p5_chessGame_bp
app.register_blueprint(p5_chessGame_bp, url_prefix='/p5_chessGame')

from p5_monkeymen import p5_monkeymen_bp
app.register_blueprint(p5_monkeymen_bp, url_prefix='/p5_monkeymen')

from p5_calculus import p5_calculus_bp
app.register_blueprint(p5_calculus_bp, url_prefix='/p5_chessGame')


