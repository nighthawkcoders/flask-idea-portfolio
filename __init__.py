from flask import Flask
from teacher import teacher_bp

app = Flask(__name__)

# Puts the Teacher blueprint .
app.register_blueprint(teacher_bp, url_prefix='/teacher')