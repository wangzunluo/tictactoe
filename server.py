# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:36:07 2018

@author: Lucas
"""

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    print(request.args)
    return render_template('game.html')
