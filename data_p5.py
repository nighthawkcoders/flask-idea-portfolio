"""Data file for Period 1"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    EXAMPLE = model.Project("Project Name", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
                            ["Talented Student 1", "Talented Student 2", "Smart Student 3", "Team Member 4",
                             "Amazing Member 5"], "This is our fabulous project, because we are cool (description)")
    p5_calculus = model.Project("p5_calculus", "http://76.88.9.120/", "/static/img/AkaTeamCalculus.png", "calculus",
                            ["Karam Alshaikh", "Akhilesh Genneri", "Akshit Prathipati", "Noya Hafiz",
                             "Jien (Max) Wang"], "This website is used for everything calculus and to spread our information about it")


    projects = [EXAMPLE,p5_calculus]
    period = model.Period("Period 5", "Some really smart people study apcsp here", projects)
    return period