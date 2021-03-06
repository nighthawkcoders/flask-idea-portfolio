"""Data file for Period 1"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    """EXAMPLE = model.Project("Example", url_for('teacher_bp.index'), "/static/img/teacher.png", "Team Teacher",
                            ["John Mortensen", "Classroom of 40"],
                            "Visit a VANTA birds experience and learn how it is made.")
                            """

    p5_calculus = model.Project("Calculus", url_for('p5_calculus_bp.home'),
                                "/static/img/AkaTeamCalculus.png", "calculus",
                                ["Karam Alshaikh", "Akhilesh Genneri", "Akshit Prathipati", "Noya Hafiz",
                                 "Jien (Max) Wang"],
                                "This website is used for everything calculus and to spread our information about it!")

    p5_chessGame = model.Project("Chess Game", url_for('p5_chessGame_bp.index'),
                                 "/static/img/p5_chessGame.jpg", "Chess Game",
                                 ["Colin Szeto", "Devam Shrivastava", "Shekar Krishnamoorthy", "Kyle Myint",
                                  "David Kim"],
                                 "Vist Chess Game to play through our chess game!")

    p5_gorillas = model.Project("Gorillas", 'http://70.95.189.45:5000/',
                                "/static/img/p5_gorillas.png", "Gorillas",
                                ["Pedro de Medeiros", "Jagroop Vij", "Arul Salaniwal", "Manuel Villa-Hernandez",
                                 "Colin Tran"],
                                "Here you find the repositories for all our projects; our journals, where we document coding progress; and Individual pages with personal information and our coding experiences. Explore!!")

    p5_monkeymen = model.Project("San Diego Travel Website", url_for('p5_monkeymen_bp.index'),
                                 "/static/img/p5_monkeymen.jpg", "Monkey Men",
                                 ["Allen Xu", "Marc Humeau", "Jacob Nguyen", "Dadyar Khalili Samani",
                                  "Jason Francisco"],
                                 "A website that reviews wonderful places located in San Diego")

    p5_supercool = model.Project("Geo-guessr", url_for('p5_supercool_bp.landing'), "/static/img/p5_supercool.jpg", "Super Cool",
                                 ["James Hunt", "Mackenzie Aboy", "Lucas Kaimer", "Sam Koenig", "Kira Liao"],
                                 "This website is all about places in the world. Visit to learn a few cool facts and play a guesser game!")

    p5_pokemon = model.Project("Pokemon Game", "http://24.255.211.218:3000/",
                               "/static/img/p5_pokemon.jpg", "Gorillas",
                               ["Zachary Joseph", "Dayita Ray", "Adhithi NarayanaMurthy", "Aiden Cizek"],
                               "Explore the world of Pokemon, with our game and pokedex. Travel to each region to go on a journey. Battle different pokemon in our 1-2 player game.")

    p5_multimedia = model.Project("Multimedia", url_for('p5_multimedia_bp.index'), '/static/img/p5_multimedia.png',
                                  "multimedia",
                                  ["Komay Sugiyama", "Christopher Rubin", "Ridhima Inukurti", "Kian Kishimito",
                                   "Megan Corrigan"],
                                  "Search amazon, show off your youtube videos, and share your spotify playlists on this multimedia page!")

    p5_alethianews = model.Project("Alethia News Website", url_for('p5_alethianews.index'),
                                   "/static/img/p5_alethianews.jpg", "Alethia News",
                                   ["Anthony Wilson", "Ryan Shay"],
                                   "A news website that provides facts with no bias to allow society to develop their own based opinions.")

    projects = [p5_monkeymen, p5_supercool, p5_chessGame, p5_pokemon, p5_gorillas, p5_calculus,
                p5_alethianews, p5_multimedia]  # p5_monkeymen  p5_multimedia

    period = model.Period("Period 5", "Some really smart people study APCSP here", projects)
    return period
