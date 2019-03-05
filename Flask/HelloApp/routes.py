# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:55:04 2019

@author: Sharmila
"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"