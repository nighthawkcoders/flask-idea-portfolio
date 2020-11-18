from p5_gorillas import model
from flask import render_template
from p5_gorillas import p5_gorillas_bp


# app = Flask(__name__)


@p5_gorillas_bp.route('/')
def home():
    return render_template("home.html", projects=model.setup(), data=model.runtime())


@p5_gorillas_bp.route('/projects')
def projects():
    return render_template("projects.html")


@p5_gorillas_bp.route('/journals')
def journals():
    return render_template("journals.html")


@p5_gorillas_bp.route('/pedro')
def pedro():
    return render_template("pedro.html")


@p5_gorillas_bp.route('/roop')
def roop():
    return render_template("roop.html")


@p5_gorillas_bp.route('/arul')
def arul():
    return render_template("arul.html")


@p5_gorillas_bp.route('/manuel')
def manuel():
    return render_template("manuel.html")


@p5_gorillas_bp.route('/colin')
def colin():
    return render_template("colin.html")
