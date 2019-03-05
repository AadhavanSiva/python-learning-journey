# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:50:54 2019

@author: Sharmila
"""

from flask import Flask

app = Flask(__name__)

from app import routes
