"""Data file for Period 1"""

import model  # projects definitions are placed in different file
from flask import url_for



def setup():
    project1 = model.Project("Project 1", url_for('teacher_bp.index'), "/static/img/cat3.jpg", "Team Teacher",
                             ["Talented Ghost 1", "Talented Mummy 2", "Smart Witch 3"],
                            "This project is kind of funky, becuase I am a computer nerd")

    projects = [project1]
    period = model.Period("Period 1", "Java Gear Heads", projects)
    return period
