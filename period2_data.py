import data  # projects definitions are placed in different file


def setup():
    project1 = data.Project("Project 1", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
                            ["Talented Student 1", "Talented Student 2", "Smart Student 3"],
                            "This is our fabulous project, because we are cool")
    project2 = data.Project("Project 2", "http://www.facebook.com", "/static/img/cat2.png", "Another Team Name",
                            ["Talented Student 3", "Talented Student 4", "Smart Student 6"],
                            "This is another fabulous project of ours")
    project3 = data.Project("Project 3", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
                            ["Talented Student 1", "Talented Student 2", "Smart Student 3"],
                            "This is our fabulous project, because we are cool")
    project4 = data.Project("Project 4", "http://www.facebook.com", "/static/img/cat2.png", "Another Team Name",
                            ["Talented Student 3", "Talented Student 4", "Smart Student 6"],
                            "This is another fabulous project of ours")
    project5 = data.Project("Project 5", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
                            ["Talented Student 1", "Talented Student 2", "Smart Student 3"],
                            "This is our fabulous project, because we are cool")
    project6 = data.Project("Project 6", "http://www.facebook.com", "/static/img/cat2.png", "Another Team Name",
                            ["Talented Student 3", "Talented Student 4", "Smart Student 6"],
                            "This is another fabulous project of ours")
    project7 = data.Project("Project 7", "http://www.google.com", "/static/img/cat1.jpg", "Team Name",
                            ["Talented Student 1", "Talented Student 2", "Smart Student 3"],
                            "This is our fabulous project, because we are cool")
    project8 = data.Project("Project 8", "http://www.facebook.com", "/static/img/cat2.png", "Another Team Name",
                            ["Talented Student 3", "Talented Student 4", "Smart Student 6"],
                            "This is another fabulous project of ours")
    projects = [project1, project2, project3, project4, project5, project6, project7, project8]
    period = data.Period("Period 2", "Some really smart people study here", projects)
    return period
