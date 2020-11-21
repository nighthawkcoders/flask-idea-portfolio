from flask import Flask, flash, redirect, render_template, request, session
from p2_sshlogin import p2_sshlogin_bp
import os
# create a Flask instance
app = Flask(__name__)

# connects default URL of server to a python function
@p2_sshlogin_bp.route('/main')
def index():
    if not session.get('logged_in'):
        return render_template('p2_sshlogin/login.html')
    else:
        return render_template('p2_sshlogin/home.html')

@p2_sshlogin_bp.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong password!')
    return index()

@p2_sshlogin_bp.route('/links')
def links_route():
    return render_template("p2_sshlogin/links.html")

@p2_sshlogin_bp.route('/flask')
def flask():
    return render_template("p2_sshlogin/flask.html")

@p2_sshlogin_bp.route('/embedshell')
def embed():
    return render_template("p2_sshlogin/embedshell.html")

@p2_sshlogin_bp.route('/embedyoutube')
def video():
    return render_template("p2_sshlogin/embedyoutube.html")

@p2_sshlogin_bp.route('/project/journal1')
def journal1_route():
    return render_template("p2_sshlogin/definedata.html", data=data.journal1())

@p2_sshlogin_bp.route('/project/journal2')
def journal2_route():
    return render_template("definedata.html", data=data.journal2())

@p2_sshlogin_bp.route('/backgroundbeat')
def music():
    return render_template("backgroundbeat.mp3")

@p2_sshlogin_bp.route('/embedprojectplan')
def embed1():
    return render_template("p2_sshlogin/embedprojectplan.html")

@p2_sshlogin_bp.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template("p2_sshlogin/form.html")
    elif request.method == 'POST':
        if request.form.get('title') != '' and request.form.get('category') != ''  and request.form.get('description') != '' :
            title = request.form.get('title')
            category = request.form.get('category')
            description = request.form.get('description')
            return redirect("/showform?title=" + str(title) +"&category=" + str(category) + "&description=" + str(description), code=302)
        else:
            return render_template("p2_SShLogin/form.html")


@p2_sshlogin_bp.route('/showform', methods=['POST', 'GET'])
def showform():
    title = request.args.get('title')
    category = request.args.get('category')
    description = request.args.get('description')
    return render_template("p2_sshlogin/showform.html", title=title, description=description, category=category)
