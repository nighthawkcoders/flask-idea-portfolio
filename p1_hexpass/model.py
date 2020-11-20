"""Model in MVC has responsibilty of managing data or database"""


def runtime():
    greeting = "P1 Hexpass!"
    name = "Repl"
    doa = "November 19"
    job = "Runtime Link"
    embed = "https://repl.it/@ahale1/p1-hexpass?lite=true&outputonly=1"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info


def alldata():
    return [runtime()]
