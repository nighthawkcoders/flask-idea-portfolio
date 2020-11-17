"""Data file for Period 1"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    # project1 = model.Project("Project 1", url_for('teacher_bp.index'), "/static/img/cat3.jpg", "Team Teacher",
                            # ["Talented Ghost 1", "Talented Mummy 2", "Smart Witch 3"],
                            # "This project is kind of funky, becuase I am a computer nerd")
    
    p1_robotmania = model.Project("Robot Mania", url_for('p1_robotmania_bp.index'), "/static/img/p1_robotmania.png", "Robot Mania",
                             ["Nakul Nandhakumar", "Sanvi Pal", "Sara Beniwal", "Vihan Jayaraman", "Yasaswi Singamneni"],
                             "The main focus of our project was to make a bunch of fun minigames. There are some other activities "
                             "that will show up on the menu but the highlights are battleship, connect-four, and hangman.")
    
    projects = [p1_robotmania]
    period = model.Period("Period 1", "Computer Science A", projects)
    return period
