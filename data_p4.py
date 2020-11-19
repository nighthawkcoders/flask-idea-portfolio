"""Data file for Period 4"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    """EXAMPLE = model.Project("Example", url_for('teacher_bp.index'), "/static/img/teacher.png", "Team Teacher",
                            ["John Mortensen", "Classroom of 40"],
                            "Visit a VANTA birds experience and see how it is made.")"""

    p4_slackbots = model.Project("Merch Website", "http://76.176.109.127:6969/", "/static/img/p4_slackbots.png",
                                 "P4Slackbots",
                                 ["Abhijay Deevi", "Kevin Do", "Travis Medley", "Paul Bokelman", "Gavin Theriault"],
                                 "This project is a merch website that we created for our Youtube channels, GodlyGoats and "
                                 "Albertpani Compani. We have a lot of merch you can buy and other information.")

    p4_hangman = model.Project("Music Website", url_for('p4_hangman_bp.index'), "/static/img/p4hangman.png", "P4 Hangman",
                               ["Charlie Zhu", "Rohan Nallapati", "Rivan Nayak", "Sarah Xie", "Noah Pidding"],
                               "This website includes a portfolio of our projects we worked on this trimester as well as a music section including three different genres of music with multiple examples and descriptions of each.")
    
    p4_fruitycoders = model.Project("Photography Website", "google.com", "/static/img/p4_fruitycoders.png", "P4 fruitycoders",
                               ["Sophie Lee", "Linda Long", "Maggie Killada", "Adam Holbel", "Wenshi Bao"],
                               "Our website (Fruity Photos) features the history of photography, as well as the works and biographies of several famous photographers, such as Ansel Adams and Annie Leibovitz.")


    projects = [p4_slackbots, p4_hangman, p4_fruitycoders]
    period = model.Period("Period 4", "AP Principles of Computer Science - Python", projects)
    return period
