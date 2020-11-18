def playdata():
    greeting = "Hello,"
    name = "Charlie"
    dob = "February 2nd"
    job = "None"
    story = "I am a junior at Del Norte High School. I was born in San Diego" \
            " and am currently 16 years old. I have an older sister who is in college. " \
            "Some things I like to do in my free time are play video games and run."
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story}
    return info


def playdata2():
    greeting = "Hey"
    name = "Rohan"
    dob = "January 1st"
    job = "None"
    story = "I am a 16 year old Junior at Del Norte High School and I was born in Austin, Texas. " \
            "I have one younger brother in the 9th grade who also goes to DNHS. Things I enjoy doing " \
            "in my free time are eating, reading, and playing video games."
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story}
    return info


def playdata3():
    greeting = "What up"
    name = "Sarah"
    dob = "May 10th"
    job = "instructor at NexStream Tech"
    story = "I'm a junior at DNHS. I was born in Ontario, Canada and I moved to " \
            "San Diego when I was 10. I'm allergic to shellfish and most animals. " \
            "I have an older sister who is 10 years older than me. In my free time, I like to invest in risky stocks," \
            " do design-related things, and play video games."
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story}
    return info


def playdata4():
    greeting = "Hello"
    name = "Rivan"
    dob = "November 29th"
    job = "None"
    story = "I'm a senior at DNHS. I am currently sixteen years old" \
            "and I love band. I have one sibling, and she is currently" \
            "in seventh grade."
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story}
    return info


def playdata5():
    greeting = "Wassup"
    name = "Noah"
    dob = "Mar 23"
    job = "cashier at Los Primos"
    story = "I am a senior at Del Norte High School. I was born in San Diego" \
            " and am currently 17 years old. I have an older brother who is in college, " \
            "as well as 2 younger sisters, one in high school and one in middle school.  " \
            "Some things I like to do in my free time are play video games and sports (mainly soccer)"
    info = {"greeting": greeting, "name": name, "dob": dob, "job": job, "story": story}
    return info


def playlist():
    return [playdata(), playdata2(), playdata3(), playdata4(), playdata5()]

#  Data "setup" for Projects
#  next step would be to extract project data from a database


def setup():
    #  Person Data
    title = "Charlie-A Portfolio"
    name = "Charlie, Rohan, Sarah, Rivan, Noah"
    source = {
        "name": name,
        "title": title,
    }
    #  Project Data
    project1 = "Hello Series"
    projlinks1 = [
        Link(
            "Project Plan",
            "https://docs.google.com/document/d/1fl0xDhyVlljBU_9vBKrwyA1KdtyL13fyFEHq5LzqP-A/edit?usp=sharing"
        ),
        Link("Repl", "https://repl.it/@charliezhu1/Hangman#README.md"),
        Link(
            "Journals",
            "https://docs.google.com/document/d/1fioQivtuh1K1jUl7TWyhOu3eaMYt7DtLRx1GFxRu-Xw/edit?usp=sharing"
        )
    ]
    project2 = "Flask Project"
    projlinks2 = [
        Link(
            "Project Plan",
            "https://docs.google.com/document/d/1IbB0bGAwiSk8j68Wcs0m1TMWh8LOb2xa7dvgEmebQjc/edit"
        ),
        Link("Repl", "https://repl.it/@charliezhu1/Projectexploring#main.py"),
        Link(
            "Journals",
            "https://docs.google.com/document/d/1fioQivtuh1K1jUl7TWyhOu3eaMYt7DtLRx1GFxRu-Xw/edit?usp=sharing"
        )
    ]
    #  Project Objects
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    #  HTML Data
    projects = Projects(source, [proj1, proj2])
    return projects


#  Link class contains button (label) and hypertext reference (href)
class Link:
    #  link data with button and href (url)
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href

    def get_btn(self):
        return self.btn

    def get_href(self):
        return self.href


#  Project data class contain project name and links (Link class objects)
class Project:
    #  project data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links

    def get_name(self):
        return self.name

    def get_links(self):
        return self.links


#  Projects class contains person (owner) and multiple projects (Project class objects)
class Projects:
    #  HTML data with source and projects
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects

    #  source data getter
    def get_source(self):
        return self.source

    #  project data getter
    def get_projects(self):
        return self.projects
