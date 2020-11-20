def tetris():
    greeting = "Try and Play!"
    name = "tetris"
    doa = "#"
    job = "#"
    embed = "https://tetris.smrsan761.repl.co/"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def mario():
    greeting = "Try a basic version of Mario here!"
    name = "Mario"
    doa = "#"
    job = "#"
    embed = "https://supermarioemulator.com/mario.php"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def hangman():
    greeting = "Hey!"
    name = "Hangman"
    doa = "#"
    job = "#"
    embed = "https://www.coolmathgames.com/0-hangman"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def pacman():
    greeting = "Try it out!"
    name = "PacMan"
    doa = "#"
    job = "#"
    embed = "https://elgoog.im/pacman/"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def crazy():
    greeting = "Code, Code, Code!"
    name = "Gist"
    doa = "October 2"
    job = "Code Sample"
    gist = "https://gist.github.com/jm1021/cfb277c7357e02fcb4123a6c7429a5c1.js"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "gist": gist}
    return info

def monkey():
    greeting = "Try it out!"
    name = "MonkeyMath"
    doa = "#"
    job = "#"
    embed = "https://repl.it/@lukemanning224/P4bang#README.md"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def alldata():
    return [tetris(), mario(), hangman(), pacman(), crazy(), monkey()]

def runtime():
    greeting = "Hey, Hey, Hey!"
    name = "Repl"
    doa = "October 30"
    job = "Runtime Link"
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def planning():
    greeting = "Hey, Hey!"
    name = "Padlet"
    doa = "October 23"
    job = "Project Planning"
    embed = "https://padlet.com/jmortensen7/csptime1_2"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def journal():
    greeting = "Hey!"
    name = "Google Doc"
    doa = "October 16"
    job = "Journal Record"
    embed = "https://docs.google.com/document/d/1Om-4ns6kmzePFvCB2WAyXArEHLUvKVWcQ7jVwswtX-0/edit"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def playground():
    greeting = "Play, Play, Play!"
    name = "Replit"
    doa = "October 9"
    job = "Playground"
    embed = "https://repl.it/@jmort1021/Python-Hello-Series?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def code():
    greeting = "Code, Code, Code!"
    name = "Gist"
    doa = "October 2"
    job = "Code Sample"
    gist = "https://gist.github.com/jm1021/cfb277c7357e02fcb4123a6c7429a5c1.js"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "gist": gist}
    return info

def alldata():
    return [runtime(), planning(), journal(), playground(), code()]

def playdata():
    greeting = "What's Up"
    name = "Nathan Lee"
    dob = "September 27"
    job = "Student"
    story = "I have been working on the nav bar and worked on the history of Tetris."
    embed = "https://docs.google.com/presentation/d/1UwtHx1CuNaf8BKTugaBryQUDw5UA3mnqIGHzcblct0c/edit?usp=sharing"
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story, "embed": embed}
    return info

def playdata2():
    greeting = "Hey!"
    name = "Aiden Tung"
    dob = "September 18"
    job = "Student"
    story = "I have been learning how to insert and resize images while working on my part of the website, the history of super mario."
    embed = "https://docs.google.com/presentation/d/1-zesTnpihsksij4XkXu1oszIiYEoGnDxvgGWncpFhKA/edit?usp=sharing"
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story, "embed": embed}
    return info


def playdata3():
    greeting = "Hey!"
    name = "Ryan Luo"
    dob = "September 2"
    job = "Student"
    story = "I have been learning how to change fonts and incorporate pictures into our website. I am also responsible for the history of hangman."
    embed = "https://docs.google.com/presentation/d/1aLmkUL7FpbbNmGS-C-xQX7d_RyrK0bRiMp3Pblgdnwk/edit?usp=sharing"
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story, "embed": embed}
    return info

def playdata4():
    greeting = "Hi"
    name = "Luke Manning"
    dob = "February 14"
    job = "Student"
    story = "I have been working on figuring out how to properly format the section of the website I will be given. This section will be about the history of Pacman"
    embed = "https://docs.google.com/presentation/d/1HPdry90KJi5Y3TqhCe4nNMkt-ED34kKB_gLsL0GVNxY/edit#slide=id.p"
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story, "embed": embed}
    return info

def playlist():
    return [playdata(), playdata2(), playdata3(), playdata4()]

#Data "setup" for Projects
#next step would be to extract project data from a database
def setup():
    #Source Data
    name = "Nighthawk Coding"
    github = "https://github.com/nathanlee27"
    linkedin = "https://www.linkedin.com/in/john-mortensen-1021/"
    youtube = "https://www.youtube.com/channel/UClIKOsDS5dsfzFA3zveDT3Q?view_as=subscriber"
    twitter = "https://twitter.com/NighthawkCoding"
    source = {"name": name, "github": github, "linkedin": linkedin, "youtube": youtube, "twitter": twitter}
    #Project Data
    project1 =  "Hello Series"
    projlinks1 = [
        Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
        Link("Repl", "https://repl.it/@jmort1021/Python-Hello-Series#README.md"),
        Link("Resources", "https://padlet.com/jmortensen7/csp2021")
    ]
    project2 =  "Flask Project"
    projlinks2 = [
        Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
        Link("Repl", "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?__cf_chl_jschl_tk__=cff72504752e89d50dea999ce10f859a17ecc294-1603026111-0-AdBP5FO-3nyUc_KVdPlNwvXM4MwUXy1HXHmbiJui1YBnUTPJZ8X4UBZVeYUXrnwRBJVvku9NftGYDWtp8lp4KovKX55R8S4twedzHpa2snwLwoAWaxuc4rgAa2l9J_rWqnNvUNcjJ8-p1V1RuTWV3lIy149lptozqAQdJnGj7PlcJxnu3YH22EXK-jl7bmdQmW9r_9fE1xp8J7sOFS3I1PMgmtoExcDIQSBBTnx1zQsyQGNS6wnuX72MAPnS_x3ZL1ETNRgFbVKpLsFJiR9ED1ErU54wyZYrUxEbZ_txHd7qY1T_s_lE6Ll8jYWHx-GulQ#main.py"),
        Link("Resources", "https://padlet.com/jmortensen7/csptime1_2")
    ]
    #Project Objects
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    #HTML Data
    projects = Projects(source, [proj1, proj2])
    return projects

#Link class contains button (label) and hypertext reference (href)
class Link():
    #link data with button and href (url)
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href
    def get_btn(self):
        return self.btn
    def get_href(self):
        return self.href

#Project data class contain project name and links (Link class objects)
class Project():
    #project data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links
    def get_name(self):
        return self.name
    def get_links(self):
        return self.links

#Projects class contains person (owner) and multiple projects (Project class objects)
class Projects():
    #HTML data with source and projects
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects
    #source data getter
    def get_source(self):
        return self.source
    #project data getter
    def get_projects(self):
        return self.projects
