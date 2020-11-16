"""Data file for Period 1"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    p5_proj1 = []
    projects = [p5_proj1]
    period = model.Period("Period 5", "Some really smart people study apcsp here", projects)
    return period
