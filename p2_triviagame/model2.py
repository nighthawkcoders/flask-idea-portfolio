def trivia():
    embed = "https://repl.it/@DaneVestal/Project-1?lite=true"
    title = "Trivia Game"
    section = {"embed": embed, "title": title}
    return section

def guess():
    embed = "https://repl.it/@idamobini/Guess-the-number-2?lite=true"
    title = "Guess the Number"
    section = {"embed": embed, "title": title}
    return section

def hangman():
    embed = "https://repl.it/@CrystalWidjaja/Hangman-1?lite=true"
    title = "Hangman"
    section = {"embed": embed, "title": title}
    return section

def reaction():
    embed = "https://repl.it/@CrystalWidjaja/reaction-time-final?lite=true"
    title = "Reaction Time"
    section = {"embed": embed, "title": title}
    return section

def madlibs():
    embed = "https://repl.it/@nivupai/MadLibs?lite=true"
    title = "Mad Libs"
    section = {"embed": embed, "title": title}
    return section

def rps():
    embed = "https://repl.it/@nivupai/RPS?lite=true"
    title = "Rock, Paper, Scissors"
    section = {"embed": embed, "title": title}
    return section

def all_games():
    return [trivia(), guess(), hangman(), reaction(), madlibs(), rps()]
