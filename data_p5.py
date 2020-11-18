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

    p5_gorillas = model.Project("p5_gorillas", "http://70.95.189.45:5000/",
                                "/static/img/p5_gorillas", "Gorillas",
                                ["Pedro de Medeiros", "Jagroop Vij", "Arul Salaniwal", "Manuel Villa-Hernandez", "Colin Tran"],
                                "Here you find the repositories for all our projects; our journals, where we document coding progress; and Individual pages with personal information and our coding experiences. Explore!!")

    projects = [p5_calculus, p5_gorillas, EXAMPLE]
    period = model.Period("Period 5", "Some really smart people study apcsp here", projects)
    return period
