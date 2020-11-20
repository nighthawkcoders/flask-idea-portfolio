from flask import render_template
from p5_calculus import p5_calculus_bp
# create a Flask instance

# connects default URL to a function
@p5_calculus_bp.route('/')
def home():
    # Flask import uses Jinga to render HTML
    return render_template("p5_calculus/home.html")


# connect to videos page
@p5_calculus_bp.route('/videos')
def video():
    return render_template("p5_calculus/videos.html")


# connects to calculator page
@p5_calculus_bp.route('/calculator')
def calulator():
    return render_template("p5_calculus/calculator.html")


# connects to journals page
@p5_calculus_bp.route('/journals')
def journals():
    return render_template("p5_calculus/journals.html")


@p5_calculus_bp.route('/quizzes')
def quizzes():
    return render_template("p5_calculus/quizzes.html")
