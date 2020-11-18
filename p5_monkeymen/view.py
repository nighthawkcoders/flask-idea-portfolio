from p5_monkeymen import model #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import  render_template

from p5_monkeymen import p5_monkeymen_bp

#connects default URL of server to render home.html
@p5_monkeymen_bp.route('/')
def home_route():
  return render_template("home.html", projects = model.setup())

#connects /hello path of server to render hello.html
@p5_monkeymen_bp.route('/beach/')
def hello_route():
  return render_template("beach.html", projects = model.setup())

#connects /flask path of server to render flask.html
@p5_monkeymen_bp.route('/park/')
def flask_route():
  return render_template("park.html", projects = model.setup())

@p5_monkeymen_bp.route('/restaurant/')
def playlist_route():
  return render_template("restaurant.html", projects = model.setup())

@p5_monkeymen_bp.route('/videos/')
def video_route():
  return render_template("video.html", projects = model.setup())




