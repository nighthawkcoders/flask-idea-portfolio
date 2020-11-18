"""Data file for Period 4"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    # EXAMPLE = model.Project("Project Name", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
    #                        ["Talented Student 1", "Talented Student 2", "Smart Student 3", "Team Member 4",
    #                          "Amazing Member 5"], "This is our fabulous project, because we are cool (description)")

    p4_slackbots = model.Project("Merch Website", "http://76.176.109.127:6969/", "/static/img/p4_slackbots.PNG", "P4Slackbots",
                                  ["Abhijay Deevi", "Kevin Do", "Travis Medley", "Paul Bokelman", "Gavin Theriault"],
                                  "This project is a merch website that we created for our Youtube channels, GodlyGoats and "
                                  "Albertpani Compani. We have a lot of merch you can buy and other information.")

    projects = [p4_slackbots]
    period = model.Period("Period 4", "Some really smart people study apcsp here", projects)
    return period


