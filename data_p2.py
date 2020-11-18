"""Data file for Period 2"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    project1 = model.Project("CypherCrypto", url_for('cyphercrypto_bp.index'), "/static/img/bgdeer.jpg", "Cryptomaniacs",
                             ["Nihar Marar", "Tyler Cloutier", "Dylan Roman", "Anthony Giustiniano", "Cherry Ding"],
                            "We use Ciphers and encrypt/decrypt messages.")
    project2 = model.Project("Project 2", "http://www.facebook.com", "/static/img/cat2.png", "Another Team Name",
                             ["Talented Student 3", "Talented Student 4", "Smart Student 6"],
                            "This is another fabulous project of ours")
    project3 = model.Project("Project 3", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
                             ["Talented Student 1", "Talented Student 2", "Smart Student 3"],
                            "This is our fabulous project, because we are cool")
    project4 = model.Project("Project 4", "http://www.facebook.com", "/static/img/cat2.png", "Another Team Name",
                             ["Talented Student 3", "Talented Student 4", "Smart Student 6"],
                            "This is another fabulous project of ours")
    project5 = model.Project("Project 5", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
                             ["Talented Student 1", "Talented Student 2", "Smart Student 3"],
                            "This is our fabulous project, because we are cool")
    project6 = model.Project("Project 6", "http://www.facebook.com", "/static/img/cat2.png", "Another Team Name",
                             ["Talented Student 3", "Talented Student 4", "Smart Student 6"],
                            "This is another fabulous project of ours")
    project7 = model.Project("Reserved by Crystal", "http://www.google.com", "/static/img/cat1.jpg", "Crystal's Team",
                             ["Crystal Widjaja", "Nivedita Rethnakar", "Ida Mobini", "Eva Gravin", "Dane Vestal"],
                            "This is our website with minigames, our portfolio, and much more!")
    project8 = model.Project("Project 8", "http://www.facebook.com", "/static/img/cat2.png", "Another Team Name",
                             ["Talented Student 3", "Talented Student 4", "Smart Student 6"],
                            "This is another fabulous project of ours")
    projects = [project1, project2, project3, project4, project5, project6, project7, project8]
    period = model.Period("Period 2", "Some really smart people study here", projects)
    return period
