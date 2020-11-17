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
<<<<<<< HEAD
app.register_blueprint(p1_mortos_bp, url_prefix='/period1/mortos')
=======
app.register_blueprint(p1_mortos_bp, url_prefix='/p1/mortos')

from p1_robotmania import p1_robotmania_bp
app.register_blueprint(p1_robotmania_bp, url_prefix='/p1_robotmania')
>>>>>>> d3d75bbd0fb656ffacda11067cd0b88b1a4be29a
