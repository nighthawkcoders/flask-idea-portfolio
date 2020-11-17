"""Data file for Period 4"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    EXAMPLE = model.Project("Project Name", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
                             ["Talented Student 1", "Talented Student 2", "Smart Student 3", "Team Member 4",
                              "Amazing Member 5"], "This is our fabulous project, because we are cool (description)")
    projects = [EXAMPLE]
    period = model.Period("Period 4", "Some really smart people study apcsp here", projects)
    return period
