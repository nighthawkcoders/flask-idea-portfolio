"""Model in frontend/backend, model according to classic MVC guidelines"""

# Project data class contain project name and links (Link class objects)
class Project:
    # project data with name and links
    def __init__(self, name, href, image, team_name, names, desc):
        self.name = name
        self.href = href
        self.image = image
        self.team_name = team_name
        self.names = names
        self.desc = desc


# Period stuff
class Period:
    # link data with button and href (url)
    def __init__(self, name, desc, projects):
        self.name = name
        self.desc = desc
        self.projects = projects

