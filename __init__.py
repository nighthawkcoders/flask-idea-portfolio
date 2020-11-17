"""_init_.py is used to define app and all blueprints"""
from flask import Flask
from teacher import teacher_bp

app = Flask(__name__)

# teacher blueprint and url with greater project

app.register_blueprint(teacher_bp, url_prefix='/teacher')


# PERIOD 1
from p1_mortos import p1_mortos_bp
app.register_blueprint(p1_mortos_bp, url_prefix='/period1/mortos')


from p1_robotmania import p1_robotmania_bp
app.register_blueprint(p1_robotmania_bp, url_prefix='/p1_robotmania')
