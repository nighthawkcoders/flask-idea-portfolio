"""Data file for Period 4"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    EXAMPLE = model.Project("Example", url_for('teacher_bp.index'), "/static/img/teacher.png", "Team Teacher",
                            ["John Mortensen", "Classroom of 40"],
                            "Visit a VANTA birds experience and see how it is made.")

    p4_slackbots = model.Project("Merch Website", "http://76.176.109.127:6969/", "/static/img/p4_slackbots.PNG",
                                 "P4Slackbots",
                                 ["Abhijay Deevi", "Kevin Do", "Travis Medley", "Paul Bokelman", "Gavin Theriault"],
                                 "This project is a merch website that we created for our Youtube channels, GodlyGoats and "
                                 "Albertpani Compani. We have a lot of merch you can buy and other information.")

    p4_hangman = model.Project("Music Website", url_for('p4_hangman_bp.index'), "/static/img/p4hangman.png", "P4 Hangman",
                               ["Charlie", "Rohan", "Rivan", "Sarah", "Noah"],
                               "This project is kind of funky, because I am a computer nerd")

    projects = [p4_slackbots, p4_hangman, EXAMPLE]
    period = model.Period("Period 4", "Some really smart people study apcsp here", projects)
    return period
