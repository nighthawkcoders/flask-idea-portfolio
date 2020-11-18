"""_init_.py is used to define app and all blueprints"""
from flask import Flask
from teacher import teacher_bp

app = Flask(__name__)

# teacher blueprint and url with greater project

app.register_blueprint(teacher_bp, url_prefix='/teacher')


# PERIOD 1
from p1_mortos import p1_mortos_bp
app.register_blueprint(p1_mortos_bp, url_prefix='/period1/mortos')

from p1_robotmania import p1_robotmania_bp
app.register_blueprint(p1_robotmania_bp, url_prefix='/p1_robotmania')

from p1_dataminers import p1_dataminers_bp
app.register_blueprint(p1_dataminers_bp, url_prefix='/period1/dataminers')

from p1_ilikeyacodeg import p1_ilikeyacodeg_bp
app.register_blueprint(p1_ilikeyacodeg_bp, url_prefix='/period1/ilikeyacodeg')
# PERIOD 2
from p2_cyphercrypto import cyphercrypto_bp
app.register_blueprint(cyphercrypto_bp, url_prefix='/p2_cyphercrypto')

# PERIOD 4

from p4_slackbots import p4_slackbots_bp
app.register_blueprint(p4_slackbots_bp, url_prefix='/p4_slackbots')



