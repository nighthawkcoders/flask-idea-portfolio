from flask import Flask, render_template, url_for
from p2_dinos import p2_dinos_bp
app = Flask(__name__)
# create a flask instance

class Projects:
    def __init__(self, projectname, repl, projectplan):
        self.projectname = projectname
        self.repl = repl
        self.projectplan = projectplan


# past 6 weeks project
GamesProject = Projects("Games Project", "https://repl.it/@NolanDEsopo/Games#README.MD",
                        "https://docs.google.com/document/d/1WtuvQZD_jODhgrxv6mhmUYqV28o_DA9hs4gDBUIGt_A/edit?usp=sharing")
# next 6 weeks project
PortfolioProject = Projects("Portfolio Project", "https://repl.it/@NoahAhooja/Flask-Website-Project#main.py",
                            "/p2_dinos/portfolio/")

AboutUs = Projects("About Us", "https://docs.google.com/document/d/1UP4h18qIo_UDeTZRaAAyzP-kb9ND54ws7vG3TVlz6b8/edit",
                        "https://docs.google.com/document/d/1UP4h18qIo_UDeTZRaAAyzP-kb9ND54ws7vG3TVlz6b8/edit")
# connects default URL of server to a python function
@p2_dinos_bp.route('/')
def home():
    return render_template("templates2/home.html", links=[GamesProject, PortfolioProject], Title="Home")

@p2_dinos_bp.route('/calculator/')
def calculator():
    return render_template('templates2/calculator.html', Title="Calculator")

calculator = Projects("Calculator", "/p2_dinos/calculator/", "")

@p2_dinos_bp.route('/portfolio/')
def portfolio():
    return render_template('templates2/portfolio.html', portfolioprojects=[calculator], Title="Portfolio")

@p2_dinos_bp.route('/aboutus/')
def aboutus():
    return render_template('templates2/aboutus.html', AboutUsInfo=AboutUs, Title="About Us")

@p2_dinos_bp.route('/games/')
def games():
    return render_template('templates2/games.html', Title="Games Arcade")