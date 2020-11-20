"""Data file for Period 2"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    '''
    EXAMPLE = model.Project("Example", url_for('teacher_bp.index'), "/static/img/teacher.png", "Team Teacher",
                            ["John Mortensen", "Classroom of 40"],
                            "Visit a VANTA birds experience and see how it is made.")'''

    cyphercrypto = model.Project("CypherCrypto", url_for('cyphercrypto_bp.index'), "/static/img/bgdeer.jpg",
                                 "Cryptomaniacs",
                                 ["Nihar Marar", "Tyler Cloutier", "Dylan Roman", "Anthony Giustiniano", "Cherry Ding"],
                                 "We use Ciphers and encrypt/decrypt messages.")

    p2_triviagame = model.Project("Website Portfolio", url_for("p2_triviagame_bp.index"), "/static/img/arcade.png",
                                  "Crystal's Team",
                                  ["Crystal Widjaja", "Nivedita Rethnakar", "Ida Mobini", "Eva Gravin", "Dane Vestal"],
                                  "This is our website with minigames, our portfolio, and much more!")

    """p2_einsteins = model.Project("Project Page", url_for('p2_einsteins_bp.home_route'), "/static/img/p2_einsteins.png",
                                 "Einsteins",
                                 ["Pragadeesh Raj", "Ayman Kazi", "Brandon Truong", "Navodit Maheshwari", "Ali Saad"],
                                 "Welcome to the world of ASCII games, intuitive text-based calculators, journal, "
                                 "reflections, individual showcases, and so much more!")"""

    p2_anime = model.Project("Plants", "http://76.176.59.209/", "/static/img/p2_anime.gif", "Anime",
                             ["Andrew Zhang", "Bradley Bartelt", "Shreya Vesant", "Diane Tang", "Nikolas Gee"],
                             "This website shows all kinds of plants and their maintnance tips")

    p2_rappers = model.Project("About Everything", 'http://107.200.91.165:5000/', "/static/img/p2_rapname.jpg",
                               "Rapper",
                               ["Sophie Bulkin", "Carter Quartararo", "Aditi Akella", "Isai Rajaraman",
                                "Mustafa Sharaf"],
                               "This is our out of this world website which will tell you about a multitude of things "
                               "such as our group and Del Norte!")

    projects = [cyphercrypto, p2_triviagame,  p2_rappers, p2_anime]#p2_einsteins,
    # projects = [cyphercrypto, p2_triviagame, p2_anime]
    period = model.Period("Period 2", "AP Principles of Computer Science - Python", projects)
    return period
