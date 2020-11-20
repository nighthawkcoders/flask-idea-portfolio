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


    p5_chessGame = model.Project("Chess Game", "https://www.youtube.com/channel/UC59JU4vWL8l0eQrixwds_3A",
                                 "/static/img/p5chessGame.jpg", "Chess Game",
                                 ["Colin Szeto", "Devam Shrivastava", "Shekar Krishnamoorthy", "Kyle Myint",
                                  "David Kim"],
                                 "Vist Chess Game to play through our chess game!")

    p5_gorillas = model.Project("Gorillas", "http://70.95.189.45:5000/",
                                "/static/img/p5_gorillas.png", "Gorillas",
                                ["Pedro de Medeiros", "Jagroop Vij", "Arul Salaniwal", "Manuel Villa-Hernandez", "Colin Tran"],
                                "Here you find the repositories for all our projects; our journals, where we document coding progress; and Individual pages with personal information and our coding experiences. Explore!!")

    """p5_monkeymen = model.Project("San Diego Travel Website", url_for('p5_monkeymen_bp.index'), "/static/img/p5_monkeymen.jpg", "Monkey Men",
                                 ["Allen Xu", "Marc Humeau", "Jacob Nguyen", "Dadyar Khalili Samani", "Jason Francisco"],
                                 "A website that reviews wonderful places located in San Diego")"""

    """
    p5_multimedia = model.Project("Multimedia", url_for("p5_multimedia_bp.index"), '/static/img/p5_multimedia.png', "multimedia", ["Komay Sugiyama", "Christopher Rubin", "Ridhima Inukurti", "Kian Kishimito", "Megan Corrigan"], "Search amazon, show off your youtube videos, and share your spotify playlists on this multimedia page!")
    """
    projects = [p5_calculus, p5_gorillas ,p5_chessGame, EXAMPLE] # p5_monkeymen  p5_multimedia

    period = model.Period("Period 5", "Some really smart people study apcsp here", projects)
    return period
