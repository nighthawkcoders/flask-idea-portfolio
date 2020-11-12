from __init__ import app

@app.route("/")
def hey_route():
    return "<h1 style='background-color:blue;color:white'>Hey Hey Hey!</h1>"

if __name__ == "__main__":
    app.run(debug=True, port="8080", host="127.0.0.1")
