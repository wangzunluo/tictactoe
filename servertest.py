# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:47:49 2018

@author: Lucas
"""

from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/<whatuwannasay>")
def sayStuff(whatuwannasay):
    return(str(whatuwannasay))