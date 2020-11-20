from p2_triviagame import p2_triviagame_bp
from p2_triviagame import model
from p2_triviagame import model2
from flask import Flask, render_template

app = Flask(__name__)

# @app.route maps specific URL to specific function-- in this case, rendering the associated html files
@p2_triviagame_bp.route('/')
def index():
    return render_template('main.html')

@p2_triviagame_bp.route('/sub')
def sub():
    return render_template('plan.html')

@p2_triviagame_bp.route('/hangman')
def hangman():
    return render_template('hangman.html')

@p2_triviagame_bp.route('/guess_the_number')
def guess_the_number():
    return render_template('guess_the_number.html')

@p2_triviagame_bp.route('/trivia')
def trivia():
    return render_template('trivia.html')

@p2_triviagame_bp.route('/reaction_time')
def reaction_time():
    return render_template('reaction_time.html')

@p2_triviagame_bp.route('/rps')
def rps():
    return render_template('rps.html')

@p2_triviagame_bp.route('/madlibs')
def madlibs():
    return render_template('madlibs.html')

@p2_triviagame_bp.route('/about')
def about():
    return render_template('about.html', aboutus=model.about()) #sets up for passing data

@p2_triviagame_bp.route('/calc')
def calc():
    return render_template('calculatorr.html')

@p2_triviagame_bp.route('/all')
def all():
    return render_template('all.html', all_page=model2.all_games()) #sets up for passing data