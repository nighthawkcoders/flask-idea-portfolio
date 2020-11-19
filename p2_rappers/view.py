from flask import Flask, render_template
from p2_rappers import p2_rappers_bp
import model

# create a Flask instance
app = Flask(__name__)


# connects default URL to a function
@p2_rappers_bp.route('/')
def index():
    # Flask import uses Jinga to render HTML
    return render_template("home.html")


@p2_rappers_bp.route('/aboutus/')
def aboutus():
    # Flask import uses Jinga to render HTML
    return render_template("aboutus.html", data=model.alldata())


@p2_rappers_bp.route('/aboutus/aditi/')
def aditi():
    # Flask import uses Jinga to render HTML
    return render_template("aditi.html", data=model.aditis_video())


@p2_rappers_bp.route('/aboutus/carter/')
def carter():
    # Flask import uses Jinga to render HTML
    return render_template("carter.html", data=model.carters_video())


@p2_rappers_bp.route('/aboutus/isai/')
def isai():
    # Flask import uses Jinga to render HTML
    return render_template("isai.html", data=model.isais_video())


@p2_rappers_bp.route('/aboutus/mustafa/')
def mustafa():
    # Flask import uses Jinga to render HTML
    return render_template("mustafa.html", data=model.mustafas_video())


@p2_rappers_bp.route('/aboutus/sophie/')
def sophie():
    sophies = [
        {
            "name": "welcome",
            "word": "code!"
        },

        {
            "name": "sophie",
            "word": "project"
        },

    ]
    # Flask import uses Jinga to render HTML
    return render_template("sophie.html", data=model.sophies_video())


@p2_rappers_bp.route('/contents/')
def contents():
    # Flask import uses Jinga to render HTML
    return render_template("contents.html")


@p2_rappers_bp.route('/aboutdn/')
def aboutdn():
    # Flask import uses Jinga to render HTML
    return render_template("aboutdn.html")


@p2_rappers_bp.route('/aboutsd/')
def sandiego():
    # Flask import uses Jinga to render HTML
    return render_template("aboutsd.html")



@p2_rappers_bp.route('/playground/')
def playground():
    # Flask import uses Jinga to render HTML
    return render_template("dropdown.html")


@p2_rappers_bp.route('/aboutsd/history/')
def sdhistory():
    # Flask import uses Jinga to render HTML
    return render_template("sdhistory.html")


@p2_rappers_bp.route('/aboutsd/landmarks/')
def sdlandmarks():
    # Flask import uses Jinga to render HTML
    return render_template("sdlandmarks.html")


@p2_rappers_bp.route('/aboutsd/tourist/')
def sdtourist():
    # Flask import uses Jinga to render HTML
    return render_template("sdtourist.html")


@p2_rappers_bp.route('/aboutsd/restaurant/')
def sdrestaurant():
    # Flask import uses Jinga to render HTML
    return render_template("sdrestaurant.html")


@p2_rappers_bp.route('/aboutsd/feedback/')
def sdfeedback():
    # Flask import uses Jinga to render HTML
    return render_template("sdfeedback.html")


@p2_rappers_bp.route("/project/journal")
def journal_route():
    return render_template("sophie.html", data=model.journal())
