"""Data file for Period 4"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    p4_hangman = model.Project("Hangman", url_for('p4_hangman_bp.index'), "/static/img/p4hangman.png", "P4 Hangman",
                               ["Charlie", "Rohan", "Rivan", "Sarah", "Noah"],
                               "This project is kind of funky, because I am a computer nerd")
    projects = [p4_hangman]
    period = model.Period("Period 4", "Hangman", projects)
    return period

