from flask import Flask, render_template

from p4_charlieb import p4_charlieb_bp

app = Flask(__name__)

#home screen
@p4_charlieb_bp.route("/home")
@p4_charlieb_bp.route("/")
def home():
  return render_template("home.html")

#playgrounds
@p4_charlieb_bp.route("/playgrounds")
def playgrounds():
  return render_template("playgrounds.html")

#themes
@p4_charlieb_bp.route("/themes")
def themes():
  return render_template("themes.html")

#github
@p4_charlieb_bp.route("/github")
def github():
  return render_template("github.html")

#project plan
@p4_charlieb_bp.route("/projectplan")
def projectplan():
  return render_template("projectplan.html")

@p4_charlieb_bp.route("/image")
def images():
  return render_template("image.html")

@p4_charlieb_bp.route("/rimages")
def rimages():
  return render_template("rimages.html")

@p4_charlieb_bp.route("/trivia")
def trivia():
  return render_template("trivia.html")

@p4_charlieb_bp.route("/rocks")
def rocks():
  return render_template("rocks.html")

@p4_charlieb_bp.route("/randomnum")
def randomnum():
  return render_template("randomnum.html")

@p4_charlieb_bp.route("/battleship")
def battleship():
  return render_template("battleship.html")

@p4_charlieb_bp.route("/kailavideo")
def kailavideo():
  return render_template("kailavideo.html")

@p4_charlieb_bp.route("/calvinvideo")
def calvinvideo():
  return render_template("calvinvideo.html")

@p4_charlieb_bp.route("/kailasgoals")
def kailasgoals():
  return render_template("kailasgoals.html")

@p4_charlieb_bp.route("/eshaangoals")
def eshaangoals():
  return render_template("eshaangoals.html")

@p4_charlieb_bp.route("/brentgoals")
def brentgoals():
  return render_template("brentgoals.html")

@p4_charlieb_bp.route("/calvingoals")
def calvingoals():
  return render_template("calvingoals.html")

@p4_charlieb_bp.route("/gametest")
def gametest():
  return render_template("gametest.html")

@p4_charlieb_bp.route("/eshaanvideo")
def eshaanvideo():
    return render_template("eshaanvideo.html")

@p4_charlieb_bp.route("/pong")
def pong():
  return render_template("pong.html")

@p4_charlieb_bp.route("/pacman")
def pacman():
  return render_template("pacman.html")

@p4_charlieb_bp.route("/tics")
def tics():
  return render_template("tics.html")

@p4_charlieb_bp.route("/snake")
def snake():
  return render_template("snake.html")

@p4_charlieb_bp.route("/brentvideo")
def brentvideo():
  return render_template("brentvideo.html")

@p4_charlieb_bp.route("/helloseries")
def helloseries():
  return render_template("helloseries.html")

@p4_charlieb_bp.route("/flask")
def flask():
  return render_template("flask.html")

@p4_charlieb_bp.route("/selfgrading")
def selfgrading():
  return render_template("selfgrading.html")

@p4_charlieb_bp.route("/journals")
def journals():
  return render_template("journals.html")
