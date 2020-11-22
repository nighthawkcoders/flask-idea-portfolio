from p5_pokemon import p5_pokemon_bp
import projects #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template,  request
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@p5_pokemon_bp.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())

#connects /hello path of server to render hello.html
@p5_pokemon_bp.route('/hello/')
def hello_route():
    return render_template("hello.html", projects=projects.setup())

#connects /flask path of server to render flask.html
@p5_pokemon_bp.route('/flask/')
def flask_route():
    return render_template("flask.html", projects=projects.setup())

@p5_pokemon_bp.route('/pokedex/')
def pokedex():
    return render_template("pokedex.html", projects=projects.setup())


@p5_pokemon_bp.route("/pokedex", methods=['GET','POST'],)


#Gather info from post, and redirects to correspodning pokedex page - Aiden
def pokemon():
    if request.method == 'POST':
        poke1 = request.form["numb1"]
        if poke1 == "1":
            return render_template("bulbasaur.html")
        if poke1 == "2":
            return render_template("charmander.html")
        if poke1 =="3":
            return render_template("squirtle.html")
        if poke1 == "4":
            return render_template("Growlithe.html")
        if poke1 =="5":
            return render_template("Staryu.html")
        if poke1 =="6":
            return render_template("Exeggcute.html")




@p5_pokemon_bp.route('/Staryu/')
def Staryu():
    return render_template("Staryu.html", projects=projects.setup())

@p5_pokemon_bp.route('/Growlithe/')
def Growlithe():
    return render_template("Growlithe.html", projects=projects.setup())

@p5_pokemon_bp.route('/bulbasaur/')
def bulbasaur():
    return render_template("bulbasaur.html", projects=projects.setup())

@p5_pokemon_bp.route('/squirtle/')
def squirtle():
    return render_template("squirtle.html", projects=projects.setup())

@p5_pokemon_bp.route('/charmander/')
def charmander():
    return render_template("charmander.html", projects=projects.setup())
