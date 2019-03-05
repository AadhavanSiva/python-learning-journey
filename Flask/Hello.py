# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:59:02 2019

@author: Sharmila
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'