import time


def setup():
    name = "Gorillas"
    github = "https://github.com/LordRoop/P5_Gorillas-Portfolio"
    youtube = "https://www.youtube.com/channel/UClIKOsDS5dsfzFA3zveDT3Q?view_as=subscriber"
    source = {"name": name, "github": github, "youtube": youtube}
    project1 = "Tic Tac Toe"
    projlinks1 = [
        Link("Project Plan", "https://docs.google.com/document/d/1TrdnML3xLl7O9xngmHF_PhhplpftU3AHa3l-TyHoe8g"),
        Link("Repl", "https://repl.it/@JSinghSD/CS-P-Tic-Tac-Toe-Groop#README.md")
    ]
    project2 = "Flask Project"
    projlinks2 = [
        Link("Project Plan", "https://docs.google.com/document/d/16C-jplZo7MnuTXzWabPOHMUYzwajv9OjvTR47Zf347o"),
        Link("Github", "https://github.com/LordRoop/P5_Gorillas-Portfolio")
    ]
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    projects = Projects(source, [proj1, proj2])
    return projects


def runtime():
    greeting = "Here you find the repositories for all our projects; our journals, where we document coding progress; and Individual pages with personal information and our coding experiences. Explore!!"
    doa = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    doah = int(time.strftime("%H", time.localtime()))
    job = "Runtime Link"
    embed = "https://Python-Web-Portfolio-Series.jmort1021.repl.co"
    info = {"greeting": greeting, "doa": doa, "doah": doah, "job": job, "embed": embed}
    return info


class Project:
    def __init__(self, name, links):
        self.name = name
        self.links = links

    def get_name(self):
        return self.name

    def get_links(self):
        return self.links


class Projects:
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects

    def get_source(self):
        return self.source

    def get_projects(self):
        return self.projects


class Link:
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href

    def get_btn(self):
        return self.btn

    def get_href(self):
        return self.href
