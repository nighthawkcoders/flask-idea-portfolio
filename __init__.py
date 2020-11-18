"""_init_.py is used to define app and all blueprints"""
from flask import Flask
from teacher import teacher_bp
from portfolio import portfolio_bp
from p1_dataminers import p1_dataminers_bp
from p1_ilikeyacodeg import p1_ilikeyacodeg_bp
from p1_mortos import p1_mortos_bp
from p1_robotmania import p1_robotmania_bp
from p2_cyphercrypto import cyphercrypto_bp
from p4_slackbots import p4_slackbots_bp
from p4_hangman import p4_hangman_bp
app = Flask(__name__)

# teacher blueprint and url with greater project

app.register_blueprint(teacher_bp, url_prefix='/teacher')
app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
app.register_blueprint(p4_hangman_bp, url_prefix='/p4_hangman')
app.register_blueprint(p1_dataminers_bp, url_prefix='/p1_dataminers')
app.register_blueprint(p1_ilikeyacodeg_bp, url_prefix='/p1_ilikeyacodeg')
app.register_blueprint(p1_mortos_bp, url_prefix='/p1_mortos')
app.register_blueprint(p1_robotmania_bp, url_prefix='/p1_robotmania')
app.register_blueprint(cyphercrypto_bp, url_prefix='/p2_cyphercrypto')
app.register_blueprint(p4_slackbots_bp, url_prefix='/p4_slackbots')