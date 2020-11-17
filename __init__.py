"""_init_.py is used to define app and all blueprints"""
from flask import Flask
from teacher import teacher_bp
from portfolio import portfolio_bp

app = Flask(__name__)

# teacher blueprint and url with greater project

app.register_blueprint(teacher_bp, url_prefix='/teacher')
app.register_blueprint(portfolio_bp, url_prefix='/portfolio')


# PERIOD 1
from p1_mortos import p1_mortos_bp
app.register_blueprint(p1_mortos_bp, url_prefix='/p1/mortos')
from p1_dataminers import p1_dataminers_bp
app.register_blueprint(p1_dataminers_bp, url_prefix='/p1/dataminers')