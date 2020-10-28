import data  # projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("home.html", projects=data.setup())


# connects /hello path of server to render hello.html
@app.route('/hello/')
def hello_rooute():
    return render_template("hello.html", projects=data.setup())


# connects /flask path of server to render flask.html
@app.route('/flask/')
def flask_route():
    return render_template("flask.html", projects=data.setup())


@app.route("/playground/")
def playground_route():
    return render_template("playground.html", data=data.playdata())


@app.route("/playlist/")
def playlist_route():
    return render_template("playlist.html", datalist=data.playlist())


@app.route("/hey/")
def heyheyhey_route():
    return "<h1 style='background-color:blue;color:white'>Hey Hey Hey!</h1>"


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
