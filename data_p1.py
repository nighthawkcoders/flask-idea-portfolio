"""Data file for Period 1"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    # project1 = model.Project("Project 1", url_for('teacher_bp.index'), "/static/img/cat3.jpg", "Team Teacher",
                            # ["Talented Ghost 1", "Talented Mummy 2", "Smart Witch 3"],
                            # "This project is kind of funky, becuase I am a computer nerd")
    
    p1_robotmania = model.Project("Robot Mania", url_for('p1_robotmania_bp.index'), "/static/img/p1_robotmania.png", "Robot Mania",
                             ["Nakul Nandhakumar", "Sanvi Pal", "Sara Beniwal", "Vihan Jayaraman", "Yasaswi Singamneni"],
                             "The main focus of our project was to make a bunch of fun minigames and a great calculator. There are some other activities "
                             "that we created but this project is mainly to show of our calculator.")
    p1_dataminers = model.Project("Dataminers", url_for('p1_dataminers_bp.index'), "/static/img/p1_dataminersTile.png", "Dataminers",
                                                  ["Andrew Pegg", "David Ramsayer", "Dominic Phung", "Michael Hayes", "Jason Chang"],
                                                  "This project has many different demos in a single program: notepad, unit converter, calculator, tic tac toe, and hangman.")

    p1_ilikeyacodeg = model.Project("I Like Ya Code G", url_for('p1_ilikeyacodeg_bp.index'), "/static/img/p1_I-like-ya-code-g.png", "I Like Ya Code G",
                                    ["Dhruv Kanetkar", "Tanay Shah", "Gautam Gupta", "Dhruv Sengupta"], "This is our Calculator Suite that allows the user to calculate a variety of things. "
                                                                                                        "It can do basic scientific calculation, convert units and binary values, sovle derivatives, and solve physics kinematic problems")
    p1_mortos = model.Project("MortOS", url_for('p1_mortos_bp.index'), "/static/img/p1_mortos-examplepic.png.jpg", "MortOS",
                             ["Nathaniel Cherian", "Benjamin Herrick", "Jett Kim", "Brendan Trinh", "Anthony Vo"],
                             "Our project was an exploration of different coding topics and concepts that's displayed through " +
                             "a variety of minigames. Try some of them out!")
    p1_grocerystoresim = model.Project("Boomer Esports", url_for('p1_grocerystoresim_bp.index'), "/static/img/p1_grocery.png", "Grocery Store Sim",
                             ["Kevin Hu", "Sean Tran", "Aditya Surapaneni", "Siddhant Ranka", "Jacob Rozenkrants"],
                             "Tired of modern flashy video games and want a blast to the past? " +
                             "Check out some of these classic games that are a nice break from the fast paced and stressful modern games.")
    p1_hexpass = model.Project("HexPass", url_for('p1_hexpass_bp.index'), "/static/img/cat2.png", "Hexpass",
                              ["Aidan Rosen", "Andrew Hale", "Andrew Joseph", "Alex Hu", "Atharva Kudrimoti"], 
                               "This project is a combination of a password manager, vector calculator and graphing calculator")
    
    p1_asciimenu = model.Project("CSA Portfolio", url_for('p1_asciimenu_bp.index'), "/static/img/natm.PNG", "CSA Portfolio",
                                       ["Neil Sahai", "Eyaad Mir", "Andrew Pu", "Alex Titov", "Sean Rollins"],
                                       "Play some games and get money to buy Calculator Functions" +
                                       "Try out some of these engaging games and remember to save some money in the ATM!")
    
    projects = [p1_robotmania, p1_dataminers, p1_ilikeyacodeg, p1_mortos, p1_grocerystoresim, p1_hexpass, p1_asciimenu] #, p1_grocerystoresim
    period = model.Period("Period 1", "Computer Science A - Java", projects)

    return period
