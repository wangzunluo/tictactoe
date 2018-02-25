# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:36:07 2018

@author: Lucas
"""
from tttFunctions import *
import json
from flask import Flask, render_template,request
import subprocess
app = Flask(__name__)
global playerNumber
global gameBoard
playerNumber = 0
gameBoard = [['','',''],['','',''],['','','']]


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
        board = json.dumps(gameBoard)
        if(playerNumber == 1):
            return(render_template('TTT.html',pnum = "X",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
        else:
                        return(render_template('TTT.html',pnum = "O",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
    elif(gameName == 'BattleShip'):
        return('We arent there yet bby')
    elif(gameName == 'polling.js'):
        return render_template('polling.js',board = board)
        
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
    bl = gameBoard[2][0]
    mr = gameBoard[1][2]
    bm = gameBoard[2][1]
    br = gameBoard[2][2]
    stat = checkStatus(gameBoard,pnum,int(row),int(col))
    if(stat[0]):
        return(render_template('endpage.html', endMessage= "Xs WON!!!!!!!",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
    elif(stat[1]):
        return(render_template('endpage.html', endMessage= "Os WON!!!!!!!",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
    elif(stat[2]):
        return(render_template('endpage.html', endMessage= "Cat game",tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))
    else:
        return(render_template('TTT.html',pnum = pnum,tl=tl,tm=tm,tr=tr,ml=ml,mm=mm,mr=mr,bl=bl,bm=bm,br=br))

@app.route('/update')
def updateBoard():
    board = json.dumps(gameBoard)
    return('polling.js',board)
@app.route("/ping")
def ping():
    data = (subprocess.check_output(["ping", "-c3", "-q", "192.168.111.100"]))
    data_crap = data.split('\n')
    # data = data.strip(data_crap[0])
    # data = data.strip(data_crap[1])
    # data = data.strip(data_crap[2])
    # data2 = data.strip(data_crap[3])
    return data_crap[3]
if __name__ == "__main__":
    app.run(host='0.0.0.0')
@app.route('/main')
def resetGame():
    global playerNumber
    global gameBoard
    playerNumber = 0
    gameBoard = [['','',''],['','',''],['','','']]
    return render_template('chooseGame.html')