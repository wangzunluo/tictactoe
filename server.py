# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:36:07 2018

@author: Lucas
"""

from flask import Flask, render_template,request
playerNumber = 0
gameBoard = [['','',''],['','',''],['','','']]

def checkWon(gameBoard):
    return False

app = Flask(__name__, template_folder="./Templates")
@app.route("/")
def chooseGame():
    print(request.url)
    return render_template('chooseGame.html')
@app.route("/game/<gameName>")
def displayGame(gameName):
    if(gameName == 'TicTacToe'):
        global playerNumber
        playerNumber += 1
        tl = gameBoard[0][0]
        tm = gameBoard[0][1]
        tr = gameBoard[0][2]
        ml = gameBoard[1][0]
        mm = gameBoard[1][1]
        mr = gameBoard[1][2]
        bl = gameBoard[2][0]
        bm = gameBoard[2][1]
        br = gameBoard[2][2]
        if(playerNumber == 1):
            return(render_template('TTT.html',pnum = "X",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
        else:
                        return(render_template('TTT.html',pnum = "O",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
    elif(gameName == 'BattleShip'):
        return('We arent there yet bby')
        
    else:
        return('wtf u doin here bro')
@app.route("/TTT/<pnum>/<row>/<col>")
def addPlay(pnum,row,col):
    gameBoard[int(row)][int(col)] = pnum
    tl = gameBoard[0][0]
    tm = gameBoard[0][1]
    tr = gameBoard[0][2]
    ml = gameBoard[1][0]
    mm = gameBoard[1][1]
    mr = gameBoard[1][2]
    bl = gameBoard[2][0]
    bm = gameBoard[2][1]
    br = gameBoard[2][2]
    won = checkWon(gameBoard)
    if(won):
                    return(render_template('TTT_won.html',pnum = "X",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
    else:
                    return(render_template('TTT.html',pnum = "X",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
@app.route("/end")
def end():
    return(render_template('endpage.html'))
        