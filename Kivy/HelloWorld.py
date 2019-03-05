# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:14:51 2019

@author: Sharmila
"""

from kivy.app import App

from kivy.uix.label import Label

class FirstKivy(App):
 
    def build(self):
 
        return Label(text="Hello Kivy!")
    

FirstKivy().run()

