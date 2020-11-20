# https://flask.palletsprojects.com/en/1.1.x/api/
from p5_chessGame import p5_chessGame_bp
from flask import Flask, render_template, request, redirect
from p5_chessGame.model import board
import model

"""import chessData
from chessData import board, movelist, allBoard
"""
#create a Flask instance
app = Flask(__name__)

#InfoDb = []

#connects default URL of server to a python function
@p5_chessGame_bp.route('/')
def home():
    #function uses Flask import (Jinga) to render HTML
    #model is passed as a parameter
    return render_template("p5_chessGame/home.html")#home has to be under templates

@p5_chessGame_bp.route("/project/chessJs/")#for the dragable chess file
def chessJS():
  return render_template("p5_chessGame/chessJs.html")

@p5_chessGame_bp.route("/project/chessPush/")#for the print chess board from dictonaries
def chessPush():
    return render_template("p5_chessGame/chessPush.html", displayBoard=board)

"""@p5_chessGame_bp.route("/project/index/")#for the dragable chess file
def index():
    return render_template("p5_chessGame/index.html", display="")"""

@p5_chessGame_bp.route("/project/index/")#for the dragable chess file
def index():
    return render_template("p5_chessGame/chessEmbed.html")

@p5_chessGame_bp.route("/project/add/", methods=['GET','POST'],)#for the dragable chess file
def addition():
    if request.method == 'POST':
        form = request.form
        numberOne = int(form['numOne'])
        numberTwo = int(form['numTwo'])
        calc = numberOne + numberTwo
        return render_template("p5_chessGame/index.html", your_list = model.answersdata(calc))#model.playlist()

    return redirect("p5_chessGame/index")


@p5_chessGame_bp.route("/project/yourName/", methods=['GET','POST'],)#for the dragable chess file
def yourName():
    if request.method == 'POST':
        form = request.form
        name = int(form['name'])
        return render_template("p5_chessGame/index.html", name = name)
    return redirect("p5_chessGame/nameBack")


@p5_chessGame_bp.route("/project/journals/")#for storing all the links to the webpage
def journals():
  return render_template("p5_chessGame/journals.html")#,repl="repl of website", website ="link to personal website")#allows to define the text that is hyperlinked on the the personal journals

@p5_chessGame_bp.route("/project/chessEmbed/")
def chessEmbed():
    return render_template("p5_chessGame/chessEmbed.html")


"""
#--------------------------------------------------- here is where the chess with POST starts
@p5_chessGame_bp.route("/project/chessMenu/") # this gets the user to the chess board
def chessMenu():
    return render_template("chessMenu.html")

@p5_chessGame_bp.route("/project/chessDictTable/") # this gets the user to the chess board
def chessDictTable_route():
    return render_template("chessDictTable.html")

@p5_chessGame_bp.route("/createBoardTable", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def createBoardTable():
    if request.method == 'POST': #if the meathod is post
        form = request.form
        movelist.clear()#resets the stored moves when create board is selected
        return render_template("chessDictTable.html", rowList=board,  displayClicked="  ", allBoard=allBoard)
        #board1=board1, board2=board2, board3=board3, board4=board4, board5=board5, board6=board6, board7=board7, board8=board8
    return redirect("/project/chessDictTable/") #redirects to format into the chess board

"""
"""
@p5_chessGame_bp.route("/firstValue", methods=['GET','POST'])
def returnClicked():
    if request.method == 'POST':
        form = request.form
        #input = str(form['value'])
        return render_template("chessDictTable.html", rowList=board,  displayClicked="you clicked something", allBoard=allBoard)
    return redirect("/project/chessDictTable/")

@p5_chessGame_bp.route("/a8", methods=['GET','POST'])#--------------------------------------------------------------------------------------------------------------------------------------------------------------this is where it starts
def a8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board, displayClicked="a8", allBoard=allBoard, movelist=chessData.movesdata("a8"), message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/a7", methods=['GET','POST'])
def a7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a7", allBoard=allBoard, movelist=chessData.movesdata("a7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/a6", methods=['GET','POST'])
def a6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a6", allBoard=allBoard, movelist=chessData.movesdata("a6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/a5", methods=['GET','POST'])
def a5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a5", allBoard=allBoard, movelist=chessData.movesdata("a5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/a4", methods=['GET','POST'])
def a4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a4", allBoard=allBoard, movelist=chessData.movesdata("a4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/a3", methods=['GET','POST'])
def a3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a3", allBoard=allBoard, movelist=chessData.movesdata("a3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/a2", methods=['GET','POST'])
def a2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a2", allBoard=allBoard, movelist=chessData.movesdata("a2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/a1", methods=['GET','POST'])
def a1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="a1", allBoard=allBoard, movelist=chessData.movesdata("a1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/b8", methods=['GET','POST'])
def b8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b8", allBoard=allBoard, movelist=chessData.movesdata("b8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/b7", methods=['GET','POST'])
def b7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b7", allBoard=allBoard, movelist=chessData.movesdata("b7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/b6", methods=['GET','POST'])
def b6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b6", allBoard=allBoard, movelist=chessData.movesdata("b6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/b5", methods=['GET','POST'])
def b5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b5", allBoard=allBoard, movelist=chessData.movesdata("b5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/b4", methods=['GET','POST'])
def b4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b4", allBoard=allBoard, movelist=chessData.movesdata("b4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/b3", methods=['GET','POST'])
def b3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b3", allBoard=allBoard, movelist=chessData.movesdata("b3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/b2", methods=['GET','POST'])
def b2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b2", allBoard=allBoard, movelist=chessData.movesdata("b2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/b1", methods=['GET','POST'])
def b1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="b1", allBoard=allBoard, movelist=chessData.movesdata("b1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")

@p5_chessGame_bp.route("/c8", methods=['GET','POST'])
def c8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c8", allBoard=allBoard, movelist=chessData.movesdata("c8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/c7", methods=['GET','POST'])
def c7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c7", allBoard=allBoard, movelist=chessData.movesdata("c7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/c6", methods=['GET','POST'])
def c6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c6", allBoard=allBoard, movelist=chessData.movesdata("c6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/c5", methods=['GET','POST'])
def c5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c5", allBoard=allBoard, movelist=chessData.movesdata("c5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/c4", methods=['GET','POST'])
def c4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c4", allBoard=allBoard, movelist=chessData.movesdata("c4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/c3", methods=['GET','POST'])
def c3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c3", allBoard=allBoard, movelist=chessData.movesdata("c3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/c2", methods=['GET','POST'])
def c2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c2", allBoard=allBoard, movelist=chessData.movesdata("c2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/c1", methods=['GET','POST'])
def c1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="c1", allBoard=allBoard, movelist=chessData.movesdata("c1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")

@p5_chessGame_bp.route("/d8", methods=['GET','POST'])
def d8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d8", allBoard=allBoard, movelist=chessData.movesdata("d8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/d7", methods=['GET','POST'])
def d7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d7", allBoard=allBoard, movelist=chessData.movesdata("d7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/d6", methods=['GET','POST'])
def d6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d6", allBoard=allBoard, movelist=chessData.movesdata("d6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/d5", methods=['GET','POST'])
def d5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d5", allBoard=allBoard, movelist=chessData.movesdata("d5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/d4", methods=['GET','POST'])
def d4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d4", allBoard=allBoard, movelist=chessData.movesdata("d4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/d3", methods=['GET','POST'])
def d3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d3", allBoard=allBoard, movelist=chessData.movesdata("d3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/d2", methods=['GET','POST'])
def d2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d2", allBoard=allBoard, movelist=chessData.movesdata("d2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/d1", methods=['GET','POST'])
def d1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="d1", allBoard=allBoard, movelist=chessData.movesdata("d1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")

@p5_chessGame_bp.route("/e8", methods=['GET','POST'])
def e8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e8", allBoard=allBoard, movelist=chessData.movesdata("e8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/e7", methods=['GET','POST'])
def e7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e7", allBoard=allBoard, movelist=chessData.movesdata("e7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/e6", methods=['GET','POST'])
def e6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e6", allBoard=allBoard, movelist=chessData.movesdata("e6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/e5", methods=['GET','POST'])
def e5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e5", allBoard=allBoard, movelist=chessData.movesdata("e5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/e4", methods=['GET','POST'])
def e4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e4", allBoard=allBoard, movelist=chessData.movesdata("e4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/e3", methods=['GET','POST'])
def e3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e3", allBoard=allBoard, movelist=chessData.movesdata("e3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/e2", methods=['GET','POST'])
def e2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e2", allBoard=allBoard, movelist=chessData.movesdata("e2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/e1", methods=['GET','POST'])
def e1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="e1", allBoard=allBoard, movelist=chessData.movesdata("e1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")

@p5_chessGame_bp.route("/f8", methods=['GET','POST'])
def f8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f8", allBoard=allBoard, movelist=chessData.movesdata("f8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/f7", methods=['GET','POST'])
def f7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f7", allBoard=allBoard, movelist=chessData.movesdata("f7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/f6", methods=['GET','POST'])
def f6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f6", allBoard=allBoard, movelist=chessData.movesdata("f6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/f5", methods=['GET','POST'])
def f5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f5", allBoard=allBoard, movelist=chessData.movesdata("f5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/f4", methods=['GET','POST'])
def f4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f4", allBoard=allBoard, movelist=chessData.movesdata("f4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/f3", methods=['GET','POST'])
def f3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f3", allBoard=allBoard, movelist=chessData.movesdata("f3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/f2", methods=['GET','POST'])
def f2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f2", allBoard=allBoard, movelist=chessData.movesdata("f2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/f1", methods=['GET','POST'])
def f1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="f1", allBoard=allBoard, movelist=chessData.movesdata("f1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")

@p5_chessGame_bp.route("/g8", methods=['GET','POST'])
def g8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g8", allBoard=allBoard, movelist=chessData.movesdata("g8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/g7", methods=['GET','POST'])
def g7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g7", allBoard=allBoard, movelist=chessData.movesdata("g7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/g6", methods=['GET','POST'])
def g6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g6", allBoard=allBoard, movelist=chessData.movesdata("g6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/g5", methods=['GET','POST'])
def g5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g5", allBoard=allBoard, movelist=chessData.movesdata("g5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/g4", methods=['GET','POST'])
def g4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g4", allBoard=allBoard, movelist=chessData.movesdata("g4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/g3", methods=['GET','POST'])
def g3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g3", allBoard=allBoard, movelist=chessData.movesdata("g3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/g2", methods=['GET','POST'])
def g2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g2", allBoard=allBoard, movelist=chessData.movesdata("g2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/g1", methods=['GET','POST'])
def g1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="g1", allBoard=allBoard, movelist=chessData.movesdata("g1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")

@p5_chessGame_bp.route("/h8", methods=['GET','POST'])
def h8():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h8", allBoard=allBoard, movelist=chessData.movesdata("h8"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/h7", methods=['GET','POST'])
def h7():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h7", allBoard=allBoard, movelist=chessData.movesdata("h7"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/h6", methods=['GET','POST'])
def h6():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h6", allBoard=allBoard, movelist=chessData.movesdata("h6"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/h5", methods=['GET','POST'])
def h5():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h5", allBoard=allBoard, movelist=chessData.movesdata("h5"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/h4", methods=['GET','POST'])
def h4():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h4", allBoard=allBoard, movelist=chessData.movesdata("h4"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/h3", methods=['GET','POST'])
def h3():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h3", allBoard=allBoard, movelist=chessData.movesdata("h3"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/h2", methods=['GET','POST'])
def h2():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h2", allBoard=allBoard, movelist=chessData.movesdata("h2"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
@p5_chessGame_bp.route("/h1", methods=['GET','POST'])
def h1():
    if request.method == 'POST':
        return render_template("chessDictTable.html", rowList=board,  displayClicked="h1", allBoard=allBoard, movelist=chessData.movesdata("h1"),  message=chessData.sample(len(movelist),chessData.movelist[-2:]))
    return redirect("/project/chessDictTable/")
"""
""" wil delete in accourace to step 7

if __name__ == "__main__":
    #runs the application on the repl development server
    p5_chessGame_bp.run(debug=True)
    """