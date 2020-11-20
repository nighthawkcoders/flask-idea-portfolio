from flask import render_template
from portfolio import portfolio_bp

@portfolio_bp.route('/')
def home():
    return render_template("portfolio/home.html")