"""Data file for Period 4"""

import model  # projects definitions are placed in different file


def setup():
    p4_proj1 = []
    projects = [p4_proj1]
    period = model.Period("Period 4", "Some really smart people study apcsp here", projects)
    return period
