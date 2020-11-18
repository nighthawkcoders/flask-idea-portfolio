"""_init_.py is used to define app and all blueprints"""
from flask import Flask
from teacher import teacher_bp
from portfolio import portfolio_bp
from p4_hangman import p4_hangman_bp

app = Flask(__name__)

# teacher blueprint and url with greater project

app.register_blueprint(teacher_bp, url_prefix='/teacher')
app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
app.register_blueprint(p4_hangman_bp, url_prefix='/p4_hangman')
