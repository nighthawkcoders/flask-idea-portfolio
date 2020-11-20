"""Model in MVC has responsibilty of managing data or database"""
def runtime():
    greeting = "P1 The Coders"
    name = "Repl"
    doa = "November 18"
    job = "Press play"
    embed = "https://repl.it/@DaMeanGreenBean/TheCoders?lite=true&outputonly=1"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info


def alldata():
    return [runtime()]