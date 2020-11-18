"""Data file for Period 2"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    EXAMPLE = model.Project("Example", url_for('teacher_bp.index'), "/static/img/teacher.png", "Team Teacher",
                            ["John Mortensen", "Classroom of 40"],
                            "Visit a VANTA birds experience and see how it is made.")

    cyphercrypto = model.Project("CypherCrypto", url_for('cyphercrypto_bp.index'), "/static/img/bgdeer.jpg",
                                 "Cryptomaniacs",
                                 ["Nihar Marar", "Tyler Cloutier", "Dylan Roman", "Anthony Giustiniano", "Cherry Ding"],
                                 "We use Ciphers and encrypt/decrypt messages.")

    minigames = model.Project("Website Portfolio", "http://www.google.com", "/static/img/arcade.png", "Crystal's Team",
                              ["Crystal Widjaja", "Nivedita Rethnakar", "Ida Mobini", "Eva Gravin", "Dane Vestal"],
                              "This is our website with minigames, our portfolio, and much more!")

    projects = [cyphercrypto, minigames, EXAMPLE]
    period = model.Period("Period 2", "Some really smart people study here", projects)
    return period
