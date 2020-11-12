"""_init_.py is used to define app and all blueprints"""
from flask import Flask
from teacher import teacher_bp

app = Flask(__name__)

#teacher blueprint and url with greater project
app.register_blueprint(teacher_bp, url_prefix='/teacher')