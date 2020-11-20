from flask import Flask, redirect, url_for, render_template

from .model import kevin, abhijay, paul, travis, gavin, groupdata

from p4_slackbots import p4_slackbots_bp

#@p4_slackbots_bp.route("/landing")
#def landing():
#	return render_template("landing.html")

@p4_slackbots_bp.route('/')
def startprogram():
	return render_template("apcoxgg.html")

#@p4_slackbots_bp.route("/home")


@p4_slackbots_bp.route('/slackbots/')
def slackbots():
	return render_template("about.html", groupdatalist=groupdata())

@p4_slackbots_bp.route('/kevin/')
def kevin():
	return render_template("indivabout.html", data=kevin())

@p4_slackbots_bp.route('/abhijay/')
def abhijay():
	return render_template("indivabout.html", data=abhijay())

@p4_slackbots_bp.route('/paul/')
def paul():
	return render_template("indivabout.htm", data=paul())

@p4_slackbots_bp.route('/travis/')
def travis():
	return render_template("indivabout.html", data=travis())

@p4_slackbots_bp.route('/gavin/')
def gavin():
	return render_template("indivabout.html", data=gavin())

@p4_slackbots_bp.route('/baseview/')
def baseview():
	return render_template("base-productview.html")

@p4_slackbots_bp.route('/shoebaseview/')
def shoebaseview():
	return render_template("base-productview-shoe.html")

@p4_slackbots_bp.route('/APCOFluid/')
def APCOFluid():
	return render_template("apco-fluid.html")

@p4_slackbots_bp.route('/APCOSuperstar/')
def APCOSuperstar():
	return render_template("apco-superstar.html")

@p4_slackbots_bp.route('/GGFireworks/')
def GGFireworks():
	return render_template("gg-fireworks.html")

@p4_slackbots_bp.route('/GGSuperstar/')
def GGSuperstar():
	return render_template("gg-superstar.html")

@p4_slackbots_bp.route('/Products/')
def Products():
	return render_template("products.html")

@p4_slackbots_bp.route('/Cart/')
def Cart():
	return render_template("cart.html")
