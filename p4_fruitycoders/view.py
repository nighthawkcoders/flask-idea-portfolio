from flask import Flask, render_template,redirect,url_for
import data

app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("home.html", title = data.setup())

@app.route('/history/')
def hello_route():
    return render_template("history.html")

@app.route('/biographies/')
def biographies_route():
    return render_template("biographies.html")

@app.route('/aboutus/')
def aboutus_route():
    return render_template("aboutus.html")

@app.route('/adams/')
def adams_route():
    return render_template("adams.html")

@app.route('/bourke/')
def bourke_route():
    return render_template("bourke.html")

@app.route('/goldin/')
def goldin_route():
    return render_template("goldin.html")

@app.route('/leibovitz/')
def leibovitz_route():
    return render_template("leibovitz.html")

@app.route('/mann/')
def mann_route():
    return render_template("mann.html")

@app.route('/mccurry/')
def mccurry_route():
    return render_template("mccurry.html")

@app.route('/newman/')
def newman_route():
    return render_template("newman.html")

@app.route('/pretty/')
def pretty_route():
    return render_template("pretty.html")

@app.route('/shabazz/')
def shabazz_route():
    return render_template("shabazz.html")

@app.route('/wong/')
def wong_route():
    return render_template("wong.html")

if __name__ == "__main__":
    app.run(debug = True, port=9090)