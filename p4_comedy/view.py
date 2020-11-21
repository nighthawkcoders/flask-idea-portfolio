 #projects definitions are placed in different file

from p4_comedy import p4_comedy_bp
from .model import setup

# https://flask.palletscom/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@p4_comedy_bp.route('/')
def home_route():
  return render_template("p4_comedy/home.html", projects=setup())

#connects /hello path of server to render comediandecades.html
@p4_comedy_bp.route('/comediandecades/')
def comediandecades_route():
  return render_template("p4_comedy/comediandecades.html", projects=setup())

#connects /historyofcomedy path of server to render historyofcomedy.html
@p4_comedy_bp.route('/historyofcomedy/')
def historyofcomedy_route():
  return render_template("p4_comedy/historyofcomedy.html", projects=setup())

#connects /knock path of server to render knock.html
@p4_comedy_bp.route('/knock')
def knock_route():
  return render_template("p4_comedy/knock.html", projects=setup())
  
#connects /iniyaa path of server to render iniyaa.html
@p4_comedy_bp.route('/iniyaa')
def iniyaa_route():
  return render_template("p4_comedy/iniyaa.html", projects=setup())

#connects /ketki path of server to render ketki.html
@p4_comedy_bp.route('/ketki')
def ketki_route():
  return render_template("p4_comedy/ketki.html", projects=setup())

#connects /ava path of server to render ava.html
@p4_comedy_bp.route('/ava')
def ava_route():
  return render_template("p4_comedy/ava.html", projects=setup())

#connects /lucas path of server to render lucas.html
@p4_comedy_bp.route('/lucas')
def lucas_route():
  return render_template("p4_comedy/lucas.html", projects=setup())

#connects /submit path of server to render submit.html
@p4_comedy_bp.route('/submit')
def submit_route():
  return render_template("p4_comedy/submit.html", projects=setup())

@p4_comedy_bp.route("/playground")
def playground_route():
  return render_template("p4_comedy/playground.html")
