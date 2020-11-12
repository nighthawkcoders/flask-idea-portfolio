from flask import url_for, redirect

from __init__ import app

@app.route("/")
def root_route():
    return redirect(url_for('teacher_bp.root_route'))

if __name__ == "__main__":
    app.run(debug=True, port="8080", host="127.0.0.1")
