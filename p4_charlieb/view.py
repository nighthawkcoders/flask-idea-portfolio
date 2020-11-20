from flask import Flask, render_template

from p4_charlieb import p4_charlieb_bp

app = Flask(__name__)

#home screen
@p4_charlieb_bp.route("/home")
def home():
  return render_template("p4_charlieb/home.html")

#playgrounds
@p4_charlieb_bp.route("/playgrounds")
def playgrounds():
  return render_template("p4_charlieb/playgrounds.html")

#themes
@p4_charlieb_bp.route("/themes")
def themes():
  return render_template("p4_charlieb/themes.html")

#github
@p4_charlieb_bp.route("/github")
def github():
  return render_template("p4_charlieb/github.html")

#project plan
@p4_charlieb_bp.route("/projectplan")
def projectplan():
  return render_template("p4_charlieb/projectplan.html")

@p4_charlieb_bp.route("/image")
def images():
  return render_template("p4_charlieb/image.html")

@p4_charlieb_bp.route("/rimages")
def rimages():
  return render_template("p4_charlieb/rimages.html")

@p4_charlieb_bp.route("/trivia")
def trivia():
  return render_template("p4_charlieb/trivia.html")

@p4_charlieb_bp.route("/rocks")
def rocks():
  return render_template("p4_charlieb/rocks.html")

@p4_charlieb_bp.route("/randomnum")
def randomnum():
  return render_template("p4_charlieb/randomnum.html")

@p4_charlieb_bp.route("/battleship")
def battleship():
  return render_template("p4_charlieb/battleship.html")

@p4_charlieb_bp.route("/kailavideo")
def kailavideo():
  return render_template("p4_charlieb/kailavideo.html")

@p4_charlieb_bp.route("/calvinvideo")
def calvinvideo():
  return render_template("p4_charlieb/calvinvideo.html")

@p4_charlieb_bp.route("/kailasgoals")
def kailasgoals():
  return render_template("p4_charlieb/kailasgoals.html")

@p4_charlieb_bp.route("/eshaangoals")
def eshaangoals():
  return render_template("p4_charlieb/eshaangoals.html")

@p4_charlieb_bp.route("/brentgoals")
def brentgoals():
  return render_template("p4_charlieb/brentgoals.html")

@p4_charlieb_bp.route("/calvingoals")
def calvingoals():
  return render_template("p4_charlieb/calvingoals.html")

@p4_charlieb_bp.route("/gametest")
def gametest():
  return render_template("p4_charlieb/gametest.html")

@p4_charlieb_bp.route("/eshaanvideo")
def eshaanvideo():
    return render_template("p4_charlieb/eshaanvideo.html")

@p4_charlieb_bp.route("/pong")
def pong():
  return render_template("p4_charlieb/pong.html")

@p4_charlieb_bp.route("/pacman")
def pacman():
  return render_template("p4_charlieb/pacman.html")

@p4_charlieb_bp.route("/tics")
def tics():
  return render_template("p4_charlieb/tics.html")

@p4_charlieb_bp.route("/snake")
def snake():
  return render_template("p4_charlieb/snake.html")

@p4_charlieb_bp.route("/brentvideo")
def brentvideo():
  return render_template("p4_charlieb/brentvideo.html")

@p4_charlieb_bp.route("/helloseries")
def helloseries():
  return render_template("p4_charlieb/helloseries.html")

@p4_charlieb_bp.route("/flask")
def flask():
  return render_template("p4_charlieb/flask.html")

@p4_charlieb_bp.route("/selfgrading")
def selfgrading():
  return render_template("p4_charlieb/selfgrading.html")

@p4_charlieb_bp.route("/journals")
def journals():
  return render_template("p4_charlieb/journals.html")
