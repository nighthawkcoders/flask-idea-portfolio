from flask import Flask, render_template
from p5_calculus import p5_calculus_bp
# create a Flask instance
app = Flask(__name__)


# connects default URL to a function
@p5_calculus_bp.route('/')
def home():
    # Flask import uses Jinga to render HTML
    return render_template("plan.html")


# connect to videos page
@p5_calculus_bp.route('/videos')
def video():
    return render_template("videos.html")


# connects to calculator page
@p5_calculus_bp.route('/calculator')
def calulator():
    return render_template("calculator.html")


# connects to journals page
@p5_calculus_bp.route('/journals')
def journals():
    return render_template("journals.html")


@p5_calculus_bp.route('/Repository')
def Repository():
    return render_template("Repository.html")

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')
    # KK
    # Karam
