# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:36:07 2018

@author: Lucas
"""

from flask import Flask, render_template,request
playerNumber = 0
gameBoard = {'X': [], 'O': []}

def checkWon(gameBoard):
    return False

app = Flask(__name__)
@app.route("/")
def chooseGame():
    print(request.url)
    return render_template('chooseGame.html')
@app.route("/game/<gameName>")
def displayGame(gameName):
    if(gameName == 'TicTacToe'):
        global playerNumber
        playerNumber += 1
        if(playerNumber == 1):
            return(render_template('TTT.html',pnum = 'X'))
        else:
            return(render_template('TTT.html',pnum = 'O'))
    elif(gameName == 'BattleShip'):
        return('We arent there yet bby')
        
    else:
        return('wtf u doin here bro')
#@app.route("/TTT.html/<pnum>/<row>/<col>")
#def addPlay(pnum,row,col):
#    gameBoard{pnum}.append([int(row),int(col)])
#    won = checkWon(gameBoard)
#    if(won):
#        return(render_template('TTT_won.html',pnum = pnum))
#    else:
#        