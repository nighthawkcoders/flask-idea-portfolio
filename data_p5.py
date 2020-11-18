"""Data file for Period 1"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    EXAMPLE = model.Project("Example", url_for('teacher_bp.index'), "/static/img/teacher.png", "Team Teacher",
                            ["John Mortensen", "Classroom of 40"],
                            "Visit a VANTA birds experience and see how it is made.")

    p5_calculus = model.Project("p5_calculus", "https://github.com/AkhileshLG/flaskportfolio-1",
                                "/static/img/AkaTeamCalculus.png", "calculus",
                                ["Karam Alshaikh", "Akhilesh Genneri", "Akshit Prathipati", "Noya Hafiz",
                                 "Jien (Max) Wang"],
                                "This website is used for everything calculus and to spread our information about it")

    p5_monkeymen = model.Project("San Diego Travel Website", "http://www.google.com", "/static/img/p5_monkeymen.JPG", "Monkey Men",
                                 ["Allen Xu", "Marc Humeau", "Jacob Nguyen", "Dadyar Khalili Samani", "Jason Francisco"],
                                 "A website that reviews wonderful places located in San Diego")

    projects = [p5_calculus, EXAMPLE, p5_monkeymen]
    period = model.Period("Period 5", "Some really smart people study apcsp here", projects)
    return period
